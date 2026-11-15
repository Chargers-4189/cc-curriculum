#!/usr/bin/env python3
"""Used by `ccm remove`: list (or drop) the Charging Courses ids for a folder that's being removed.

    python3 tools/lms/forget.py courses/01-fundamentals/06-arrays            # show what's linked
    python3 tools/lms/forget.py --apply courses/01-fundamentals/06-arrays    # drop it from ids.yaml

Nothing on the site is touched. The pages stay on Charging Courses until you delete them there.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import publish as P  # noqa: E402

B = P.build


def linked(target: Path) -> list[tuple[str, str, str]]:
    """(section, key, activity) for every id under the folder being removed."""
    rel = P.key(target)
    out = []
    if target.parent == P.COURSES:
        cid = (P.IDS.get("courses") or {}).get(target.name)
        if cid:
            out.append(("courses", target.name, cid))
    for section in ("lessons", "checkins"):
        for k, act in (P.IDS.get(section) or {}).items():
            if k == rel or k.startswith(rel + "/"):
                out.append((section, k, act))
    homework = {P.hw_name(p.parent) for p in target.rglob("exercises/*/prompt.md")
                if B.front_matter(p)[0].get("type") == "homework"}
    if (target / "prompt.md").exists() and B.front_matter(target / "prompt.md")[0].get("type") == "homework":
        homework.add(P.hw_name(target))
    for k, act in (P.IDS.get("homework") or {}).items():
        if k in homework:
            out.append(("homework", k, act))
    return out


def checkins_pointing_at(target: Path) -> list[str]:
    """Check-ins whose `after:` lesson is inside the folder being removed."""
    hits = []
    for f in P.COURSES.glob("*/check-ins/*.yaml"):
        lesson = f.parent.parent / str(B.read_checkin(f).get("after", ""))
        if lesson == target or target in lesson.parents:
            hits.append(P.key(f))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--apply", action="store_true", help="drop the ids instead of just listing them")
    args = ap.parse_args()
    target = args.folder.resolve()
    if P.COURSES not in target.parents:
        sys.exit(f"not under courses/: {args.folder}")

    items = linked(target)
    if not args.apply:
        for section, k, act in items:
            what = {"courses": "course", "lessons": "lesson", "homework": "homework", "checkins": "check-in"}[section]
            print(f"  {what} on the site: {k}")
        for c in checkins_pointing_at(target):
            print(f"  WARNING: {c} goes after a lesson you're removing; change its after: line")
        return 0

    for section, k, act in items:
        del P.section(section)[k]
        P.STATE.pop(act, None)
    if items:
        P.write_ids()
        P.STATE_FILE.write_text(json.dumps(dict(sorted(P.STATE.items())), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
