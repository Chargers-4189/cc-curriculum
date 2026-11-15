#!/usr/bin/env python3
"""Bring edits made on Charging Courses back into a lesson's lecture.md (used by `ccm pull`).

    python3 tools/lms/pull.py                       # list pages that changed on the site
    python3 tools/lms/pull.py courses/.../01-while-loops     # show the changes and save them

The page is turned back into markdown. Practice playgrounds, quizzes, homework links and
images keep the lines they already have in lecture.md (matched in order), and links to other
pages on the site go back to normal repo links. After saving, the page counts as published, so
`ccm publish` won't skip it.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import publish as P  # noqa: E402

B = P.build
SITE_LINK = re.compile(r"^https://chargingcourses\.com/course/([0-9a-f-]+)/activity/([0-9a-f-]+)(?:#heading-(.*))?$")
SPECIAL_LINE = re.compile(r"^\[[^\]]*\]\(([^)]+)\)\s*$")
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]+\)")


class Markdown:
    """TipTap JSON -> markdown, reusing lecture.md's own lines for the site-only blocks."""

    def __init__(self, lesson: Path):
        self.lesson = lesson
        self.warnings: list[str] = []
        current = (lesson / "lecture.md").read_text(encoding="utf-8")
        self.images = IMAGE.findall(current)
        self.practice, self.quizzes, self.homework = [], [], []
        for line in current.splitlines():
            m = SPECIAL_LINE.match(line.strip())
            if not m:
                continue
            target = m.group(1)
            if target.startswith("quiz/"):
                self.quizzes.append(line.strip())
            elif target.endswith("prompt.md") and (lesson / target).exists():
                kind = B.front_matter(lesson / target)[0].get("type")
                (self.practice if kind == "practice" else self.homework).append(line.strip())
        self.used = {"image": 0, "practice": 0, "quiz": 0}
        rev = {}
        for sec in ("lessons", "homework"):
            for k, act in (P.IDS.get(sec) or {}).items():
                rev[act] = (sec, k)
        self.reverse = rev
        self.hw_dirs = {P.hw_name(e.parent): e.parent for e in P.COURSES.rglob("exercises/*/prompt.md")
                        if B.front_matter(e)[0].get("type") == "homework"}

    # ---- links back to repo paths
    def href(self, url: str) -> str:
        m = SITE_LINK.match(url)
        if not m or m.group(2) not in self.reverse:
            return url
        sec, k = self.reverse[m.group(2)]
        target = (P.COURSES / k / "lecture.md") if sec == "lessons" else (self.hw_dirs.get(k, Path()) / "prompt.md")
        rel = Path(_relpath(target, self.lesson))
        return str(rel) + (f"#{m.group(3)}" if m.group(3) else "")

    # ---- inline
    def inline(self, nodes: list[dict], outer: tuple = ("link", "bold", "italic")) -> str:
        """Groups neighbours that share a link/bold/italic mark, so `**a `b` c**` comes back in one piece."""
        nodes = list(nodes or [])
        if outer:
            mark, rest = outer[0], outer[1:]
            out, i = [], 0
            while i < len(nodes):
                key = mark_key(nodes[i], mark)
                j = i
                while j < len(nodes) and mark_key(nodes[j], mark) == key:
                    j += 1
                group = nodes[i:j]
                if key is None:
                    out.append(self.inline(group, rest))
                else:
                    inner = self.inline([strip_mark(n, mark) for n in group], rest)
                    lead = inner[:len(inner) - len(inner.lstrip())]
                    trail = inner[len(inner.rstrip()):]
                    core = inner.strip()
                    if mark == "link":
                        core = f"[{core}]({self.href(key)})"
                    else:
                        wrap = "**" if mark == "bold" else "*"
                        core = f"{wrap}{core}{wrap}"
                    out.append(lead + core + trail)
                i = j
            return "".join(out)
        out = []
        for n in nodes:
            t = n.get("type")
            if t == "text":
                out.append(self.text(n))
            elif t == "hardBreak":
                out.append("\\\n")
            elif t == "dynamicVariable":
                a = n.get("attrs") or {}
                extra = ""
                if a.get("format") or a.get("fallback"):
                    extra = f"|{a.get('format') or ''}" + (f"|{a['fallback']}" if a.get("fallback") else "")
                out.append("{{" + a.get("path", "") + extra + "}}")
            elif t == "communityTag":
                a = n.get("attrs") or {}
                out.append(f"[{a.get('name', '')}](community:{a.get('communityUuid', '')})")
            elif t == "blockImage":
                out.append(self.image())
            else:
                self.warnings.append(f"the site has a {t} that can't be written in markdown, so there's a comment in its place")
                out.append(f"<!-- site block: {t} -->")
        return "".join(out)

    def text(self, n: dict) -> str:
        s = n.get("text", "")
        marks = {m["type"]: m for m in n.get("marks") or []}
        lead = s[:len(s) - len(s.lstrip())]
        trail = s[len(s.rstrip()):]
        core = s.strip()
        if not core:
            return s
        if "code" in marks:
            tick = "``" if "`" in core else "`"
            core = f"{tick}{core}{tick}"
        else:
            core = re.sub(r"([\\*_\[\]`])", r"\\\1", core)
        return lead + core + trail

    # ---- blocks
    def image(self) -> str:
        i = self.used["image"]
        self.used["image"] += 1
        if i < len(self.images):
            return self.images[i]
        self.warnings.append("the site has a new image: download it into assets/ and fix the ![image](...) line")
        return "![image](assets/NEW-IMAGE.png)"

    def special(self, kind: str, pool: list[str], label: str) -> str:
        i = self.used[kind]
        self.used[kind] += 1
        if i < len(pool):
            return pool[i]
        self.warnings.append(f"the site has a new {label} that isn't in the repo; add it by hand")
        return f"<!-- new {label} from the site -->"

    def blocks(self, nodes: list[dict]) -> list[str]:
        out, skip_labs = [], False
        for n in nodes or []:
            t = n.get("type")
            if t == "paragraph":
                text = self.inline(n.get("content"))
                plain = "".join(c.get("text", "") for c in n.get("content") or [])
                if skip_labs and plain.startswith("In Labs: "):
                    skip_labs = False
                    continue
                if plain.startswith("📝 Open the ") and plain.endswith(" assignment"):
                    link = next((c for c in n["content"] if any(m["type"] == "link" for m in c.get("marks") or [])), None)
                    href = self.href(next(m for m in link["marks"] if m["type"] == "link")["attrs"]["href"]) if link else ""
                    match = next((h for h in self.homework if f"]({href})" in h), None)
                    out.append(match or f"[{link['text'] if link else 'Homework'}]({href})")
                    continue
                out.append(text)
            elif t == "heading":
                out.append("#" * int((n.get("attrs") or {}).get("level", 2)) + " " + self.inline(n.get("content")))
            elif t == "blockImage":
                out.append(self.image())
            elif t == "codeBlock":
                lang = (n.get("attrs") or {}).get("language") or ""
                code = "".join(c.get("text", "") for c in n.get("content") or [])
                fence = "````" if "```" in code else "```"
                out.append(f"{fence}{lang}\n{code}\n{fence}")
            elif t in ("bulletList", "orderedList"):
                out.append(self.list(n))
            elif t == "blockquote":
                out.append(quote("\n\n".join(self.blocks(n.get("content")))))
            elif t == "callout":
                kind = str((n.get("attrs") or {}).get("type", "info")).upper()
                inner = "\n\n".join(self.blocks(n.get("content")))
                out.append(quote(f"[!{kind}]\n{inner}"))
            elif t == "table":
                out.append(self.table(n))
            elif t == "horizontalRule":
                out.append("---")
            elif t == "blockQuiz":
                out.append(self.special("quiz", self.quizzes, "quiz"))
            elif t == "blockCode":
                out.append(self.special("practice", self.practice, "practice playground"))
                skip_labs = True
                continue
            else:
                self.warnings.append(f"the site has a {t} block that can't be written in markdown, so there's a comment in its place")
                out.append(f"<!-- site block: {t} -->")
            skip_labs = False
        return out

    def list(self, n: dict) -> str:
        ordered = n["type"] == "orderedList"
        start = int((n.get("attrs") or {}).get("start") or 1)
        lines = []
        for i, item in enumerate(n.get("content") or []):
            marker = f"{start + i}. " if ordered else "- "
            pad = " " * len(marker)
            parts = self.blocks(item.get("content"))
            body = ""
            for j, part in enumerate(parts):
                if j:
                    body += "\n" if part.lstrip().startswith(("- ", "1. ")) or re.match(r"^\d+\. ", part) else "\n\n"
                body += part
            first, *rest = body.split("\n")
            lines.append(marker + first + "".join("\n" + (pad + r if r else "") for r in rest))
        return "\n".join(lines)

    def table(self, n: dict) -> str:
        rows = []
        for r in n.get("content") or []:
            cells = []
            for c in r.get("content") or []:
                cells.append(" ".join(self.blocks(c.get("content"))).replace("|", "\\|"))
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            width = rows[0].count(" | ") + 1
            rows.insert(1, "|" + "---|" * width)
        return "\n".join(rows)


def mark_key(node: dict, mark: str):
    """What a node's mark is (a link's href, or True), or None if it doesn't have it."""
    for m in node.get("marks") or []:
        if m["type"] == mark:
            return (m.get("attrs") or {}).get("href", "") if mark == "link" else True
    return None


def strip_mark(node: dict, mark: str) -> dict:
    return {**node, "marks": [m for m in node.get("marks") or [] if m["type"] != mark]}


COMMENT = re.compile(r"<!--.*?-->", re.S)


def keep_repo_lines(current: str, pulled: str) -> str:
    """Use the repo's own lines wherever the only difference is spacing or comments (the site
    doesn't keep either), so pulling only changes what really changed."""
    def same(a: list[str], b: list[str]) -> bool:
        norm = lambda ls: [l.strip() for l in COMMENT.sub("", "\n".join(ls)).split("\n")
                           if l.strip() not in ("", ">")]
        return norm(a) == norm(b)
    cur, new = current.split("\n"), pulled.split("\n")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, cur, new, autojunk=False).get_opcodes():
        if op == "equal" or same(cur[i1:i2], new[j1:j2]):
            out += cur[i1:i2]
        else:
            out += new[j1:j2]
    return "\n".join(out)


def quote(text: str) -> str:
    return "\n".join(("> " + line) if line else ">" for line in text.split("\n"))


def _relpath(target: Path, base: Path) -> str:
    import os
    return os.path.relpath(target, base)


def to_markdown(lesson: Path, doc: dict) -> tuple[str, list[str]]:
    md = Markdown(lesson)
    text = "\n\n".join(b for b in md.blocks((doc or {}).get("content")) if b is not None).rstrip() + "\n"
    return text, md.warnings


def rebuild(lesson: Path, text: str) -> dict:
    """What build.py would make from this markdown (without writing it anywhere)."""
    b = B.Builder(lesson)
    content, _ = b.blocks(b.md.parse(text))
    return {"type": "doc", "content": [B.clean(c) for c in content]}


def loose(node):
    """Ignore details the editor adds on its own (link rel/target, empty attrs) when comparing."""
    if isinstance(node, dict):
        out = {k: loose(v) for k, v in node.items() if k not in ("rel", "target", "class", "title")}
        return out
    if isinstance(node, list):
        return [loose(x) for x in node]
    return node


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lesson", nargs="?", type=Path)
    ap.add_argument("-y", "--yes", action="store_true", help="save without asking")
    args = ap.parse_args()
    api = P.Api(P.token())

    if args.lesson is None:  # list what changed on the site, then offer to pull one
        found = 0
        changed = []
        with P.Spinner("Checking the site...") as spin:
            for k, act in sorted((P.IDS.get("lessons") or {}).items()):
                if not (P.COURSES / k / "lecture.md").exists():
                    continue
                spin.update(f"Checking {k}...")
                live = P.trimmed((api.get(f"/activities/activity_{act}") or {}).get("content") or {})
                if P.edited_on_site(act, live):
                    found += 1
                    why = "changed on the site" if act in P.STATE else "never published from the repo"
                    spin.echo(f"{P.paint('33', 'changed')}  {k}  ({why})")
                    changed.append(k)
        print(P.paint("2", f"{found} page(s) to pull" if found else "nothing changed on the site"))
        if not changed:
            return 0
        sys.path.insert(0, str(P.ROOT / "tools"))
        from ui import choose
        pick = choose("Pull which one?", changed + ["none"])
        if not pick or pick == "none":
            return 0
        args.lesson = P.COURSES / pick

    lesson = args.lesson.resolve()
    if not (lesson / "lecture.md").exists():
        sys.exit("ccm pull works on lessons (folders with a lecture.md)")
    act = (P.IDS.get("lessons") or {}).get(P.key(lesson))
    if not act:
        sys.exit(f"{P.key(lesson)} isn't on the site yet (it's not in tools/lms/ids.yaml)")
    live = P.trimmed((api.get(f"/activities/activity_{act}") or {}).get("content") or {})
    current = (lesson / "lecture.md").read_text(encoding="utf-8")
    text, warnings = to_markdown(lesson, live)
    text = keep_repo_lines(current, text)

    rebuilt = P.fill_images(rebuild(lesson, text), P.images(live))
    exact = json.dumps(loose(P.trimmed(rebuilt)), sort_keys=True) == json.dumps(loose(live), sort_keys=True)

    if text == current:
        print("lecture.md already matches the site.")
        if exact:
            P.remember(act, live)
        return 0
    for d in difflib.unified_diff(current.splitlines(), text.splitlines(), "repo", "site", lineterm="", n=1):
        color = "32" if d.startswith("+") else "31" if d.startswith("-") else "36" if d.startswith("@@") else "2"
        print(P.paint(color, d))
    for w in dict.fromkeys(warnings):
        print(P.paint("1;31", f"WARNING: {w}"))
    if not exact:
        print(P.paint("33", "Note: this doesn't match the site exactly, so publishing later might change a few small things on the page."))
    if not args.yes:
        if not sys.stdin.isatty():
            sys.exit("not saving without confirmation (use -y)")
        sys.path.insert(0, str(P.ROOT / "tools"))
        from ui import confirm
        if not confirm("Save this into lecture.md?"):
            sys.exit("cancelled, nothing was saved")
    (lesson / "lecture.md").write_text(text, encoding="utf-8")
    P.remember(act, live)
    print(P.paint("32", f"saved {P.key(lesson)}/lecture.md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
