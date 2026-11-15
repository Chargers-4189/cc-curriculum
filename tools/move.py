#!/usr/bin/env python3
"""Rename, renumber, or move a course, chapter, lesson, or exercise (used by `ccm mv`).

Keeps everything pointing at it working: links in other lessons, `ccm get` lines,
check-in `after:` lines, and tools/lms/ids.yaml (so the site keeps the same page).

    python3 tools/move.py courses/01-fundamentals/05-loops/02-for-loops --name for-loops
    python3 tools/move.py courses/01-fundamentals/05-loops/02-for-loops --position 1
    python3 tools/move.py courses/01-fundamentals/05-loops/02-for-loops --into courses/01-fundamentals/06-arrays
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "courses"
NUM = re.compile(r"^(e?)(\d+)-(.+)$")
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
sys.path.insert(0, str(ROOT / "tools" / "lms"))


def kind_of(p: Path) -> str:
    parts = p.relative_to(COURSES).parts
    return {1: "course", 2: "chapter", 3: "lesson", 5: "exercise"}.get(len(parts), "other")


def children(parent: Path, exercise: bool) -> list[Path]:
    folder = parent / "exercises" if exercise else parent
    if not folder.is_dir():
        return []
    pre = "e" if exercise else ""
    return sorted((p for p in folder.iterdir() if p.is_dir() and NUM.match(p.name) and
                   NUM.match(p.name).group(1) == pre), key=lambda p: int(NUM.match(p.name).group(2)))


def slug(p: Path) -> str:
    return NUM.match(p.name).group(3)


def plan_moves(src: Path, name: str | None, position: int | None, into: Path | None) -> dict[Path, Path]:
    kind = kind_of(src)
    exercise = kind == "exercise"
    old_parent = src.parent.parent if exercise else src.parent
    new_parent = into or old_parent
    want_parent = {"course": "root", "chapter": "course", "lesson": "chapter", "exercise": "lesson"}[kind]
    if into is not None and (kind_of(into) if into != COURSES else "root") != want_parent:
        sys.exit(f"a {kind} has to go into a {want_parent}")
    new_name = name or slug(src)
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", new_name):
        sys.exit("names are lowercase-with-hyphens, like for-loops")
    if new_name != slug(src) and kind in ("lesson", "exercise"):
        for p in COURSES.rglob(("e" if exercise else "") + "[0-9]*-" + new_name):
            if p.is_dir() and kind_of(p) == kind:
                sys.exit(f"{kind} names must be unique, and '{new_name}' is already used at {p.relative_to(ROOT)}")

    siblings = [p for p in children(new_parent, exercise) if p != src]
    if new_parent != old_parent or position is not None:
        pos = len(siblings) if position is None else max(0, min(len(siblings), position - 1))
        order = siblings[:pos] + [src] + siblings[pos:]
        # numbering starts where this folder's siblings already start (courses at 00, the rest at 01)
        existing = [int(NUM.match(p.name).group(2)) for p in children(new_parent, exercise)]
        first = min(existing) if existing else (0 if kind == "course" else 1)
    else:
        order = children(new_parent, exercise)
        first = None  # keep numbers, only rename
    pre = "e" if exercise else ""
    base = new_parent / "exercises" if exercise else new_parent
    moves = {}
    for i, p in enumerate(order):
        num = NUM.match(p.name).group(2) if first is None else f"{first + i:02d}"
        new = base / f"{pre}{num}-{new_name if p == src else slug(p)}"
        if new != p:
            moves[p] = new
    if not moves:
        sys.exit("nothing to change")
    return moves


def mapper(moves: dict[Path, Path]):
    def m(path: Path) -> Path:
        for old, new in moves.items():
            if path == old or old in path.parents:
                return new / path.relative_to(old)
        return path
    return m


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path)
    ap.add_argument("--name", help="new name (lowercase-with-hyphens)")
    ap.add_argument("--position", type=int, help="new spot among its siblings, starting at 1")
    ap.add_argument("--into", type=Path, help="move into this course / chapter / lesson")
    ap.add_argument("-y", "--yes", action="store_true", help="don't ask to confirm")
    args = ap.parse_args()
    src = args.src.resolve()
    if COURSES not in src.parents or kind_of(src) == "other":
        sys.exit("pick a course, chapter, lesson or exercise")
    moves = plan_moves(src, args.name, args.position, args.into.resolve() if args.into else None)
    m = mapper(moves)
    inverse = {v: k for k, v in moves.items()}

    # --- links in every markdown file, worked out before anything moves
    renamed_slugs = {}
    for old, new in moves.items():
        if kind_of(old) in ("lesson", "exercise") and slug(old) != slug(new):
            renamed_slugs[slug(old)] = slug(new)
    rewrites: dict[Path, str] = {}
    for f in COURSES.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        new_file = m(f)

        def fix(match):
            target = match.group(2)
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                return match.group(0)
            path, hash_, anchor = target.partition("#")
            old_target = Path(os.path.normpath(f.parent / path))
            new_target = m(old_target)
            if new_target == old_target and new_file == f:
                return match.group(0)
            rel = os.path.relpath(new_target, new_file.parent)
            return f"{match.group(1)}{rel}{hash_}{anchor}{match.group(3)}"

        out = LINK.sub(fix, text)
        for a, b in renamed_slugs.items():
            out = re.sub(rf"(ccm get(?: [^\n`]*?)? ){re.escape(a)}\b", rf"\g<1>{b}", out)
        if out != text:
            rewrites[f] = out

    # --- check-ins whose after: lesson moves
    checkin_fixes: dict[Path, tuple[str, str]] = {}
    warnings = []
    for f in COURSES.glob("*/check-ins/*.yaml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        after = str(data.get("after") or "")
        lesson = f.parent.parent / after
        new_lesson = m(lesson)
        if new_lesson != lesson:
            if f.parent.parent not in new_lesson.parents:
                warnings.append(f"{f.relative_to(ROOT)} goes after a lesson that's moving to another course; "
                                "change its after: line")
            else:
                checkin_fixes[f] = (after, str(new_lesson.relative_to(f.parent.parent)))

    # --- the plan
    print("This will rename:")
    for old, new in moves.items():
        print(f"  {old.relative_to(ROOT)}  ->  {new.relative_to(ROOT)}")
    if rewrites:
        print(f"and update links or `ccm get` lines in {len(rewrites)} file(s)")
    if checkin_fixes:
        print(f"and the after: line in {len(checkin_fixes)} check-in(s)")
    if kind_of(src) != "course" and src.relative_to(COURSES).parts[0] != m(src).relative_to(COURSES).parts[0]:
        warnings.append("it's moving to another course. On the site, its pages stay in the old course "
                        "until you move or delete them there.")
    for w in warnings:
        print(f"WARNING: {w}")
    print("Students' addresses for these change (for example 1.5.2 might become 1.5.1).")
    if not args.yes:
        if not sys.stdin.isatty():
            sys.exit("not moving without confirmation (use -y)")
        from ui import confirm
        if not confirm("Go ahead?"):
            sys.exit("cancelled, nothing was changed")

    # --- do it: rename through temporary names so swaps don't collide
    temps = {}
    for old in moves:
        tmp = old.with_name(old.name + ".ccm-moving")
        old.rename(tmp)
        temps[old] = tmp
    for old, new in moves.items():
        new.parent.mkdir(parents=True, exist_ok=True)
        temps[old].rename(new)
    for f, text in rewrites.items():
        m(f).write_text(text, encoding="utf-8")
    for f, (a, b) in checkin_fixes.items():
        target = m(f)
        t = target.read_text(encoding="utf-8")
        target.write_text(re.sub(rf"^after:\s*[\"']?{re.escape(a)}[\"']?\s*$", f"after: {b}", t, count=1,
                                 flags=re.M), encoding="utf-8")

    # --- ids.yaml (so publishing keeps the same pages)
    import publish as P  # noqa: E402
    changed = False
    for section in ("lessons", "chapters", "checkins"):
        sec = P.IDS.get(section) or {}
        for k in list(sec):
            nk = str(m(COURSES / k).relative_to(COURSES))
            if nk != k:
                sec[nk] = sec.pop(k)
                changed = True
    courses = P.IDS.get("courses") or {}
    for k in list(courses):
        nk = m(COURSES / k).name
        if nk != k:
            courses[nk] = courses.pop(k)
            changed = True
    hw = P.IDS.get("homework") or {}
    for a, b in renamed_slugs.items():
        if a in hw:
            hw[b] = hw.pop(a)
            changed = True
    if changed:
        P.write_ids()
    print("moved. Run `ccm cases` if you renamed exercises, then `ccm validate`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
