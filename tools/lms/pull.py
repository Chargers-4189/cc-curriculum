#!/usr/bin/env python3
"""Bring edits made on Charging Courses back into a lesson's lecture.md (used by `ccm pull`).

    python3 tools/lms/pull.py                         # pick where to look, then which pages to pull
    python3 tools/lms/pull.py courses/02-object-oriented   # check one course (or a chapter)
    python3 tools/lms/pull.py courses/.../01-while-loops   # show one lesson's changes and save them

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
            rows.append(("| " + " | ".join(cells) + " |").replace("|  |", "| |"))   # empty cells come back as "| |"
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


NUM = re.compile(r"^(\d+)-")


def name(folder: Path) -> str:
    """The name you'd type for ccm (02-shape-wars -> shape-wars)."""
    return NUM.sub("", folder.name)


def outline() -> list[tuple[str, Path]]:
    """Every course, chapter and lesson on the site, labelled like `ccm list` (2, 2.1, 2.1.2), so
    you can search by address, name or title."""
    lessons = P.IDS.get("lessons") or {}
    out = []

    def kids(d: Path) -> list[Path]:
        return sorted((c for c in d.iterdir() if c.is_dir() and NUM.match(c.name)), key=lambda c: int(NUM.match(c.name)[1]))

    for course in kids(P.COURSES):
        if not any(k.startswith(course.name + "/") for k in lessons):
            continue
        n1 = int(NUM.match(course.name)[1])
        out.append((f"{n1:<8} {name(course)}  {P.read_yaml(course / 'course.yaml').get('title') or P.lesson_title(course)}", course))
        for ch in kids(course):
            n2 = f"{n1}.{int(NUM.match(ch.name)[1])}"
            out.append((f"{n2:<8}   {name(ch)}  {P.read_yaml(ch / 'chapter.yaml').get('title') or P.lesson_title(ch)}", ch))
            for le in kids(ch):
                if P.key(le) in lessons:
                    n3 = f"{n2}.{int(NUM.match(le.name)[1])}"
                    out.append((f"{n3:<8}     {name(le)}  {P.lesson_title(le)}", le))
    return out


def lessons_under(folder: Path) -> list[Path]:
    """The lessons (on the site) inside a course, chapter or lesson folder."""
    lessons = P.IDS.get("lessons") or {}
    if (folder / "lecture.md").exists():
        return [folder]
    return [f.parent for f in sorted(folder.rglob("lecture.md")) if P.key(f.parent) in lessons]


class Pulled:
    """A lesson's page on the site, turned back into markdown."""

    def __init__(self, api: P.Api, lesson: Path):
        self.lesson = lesson
        self.act = (P.IDS.get("lessons") or {}).get(P.key(lesson))
        if not self.act:
            sys.exit(f"{P.key(lesson)} isn't on the site yet (it's not in tools/lms/ids.yaml)")
        self.live = P.trimmed((api.get(f"/activities/activity_{self.act}") or {}).get("content") or {})
        self.current = (lesson / "lecture.md").read_text(encoding="utf-8")
        text, self.warnings = to_markdown(lesson, self.live)
        self.text = keep_repo_lines(self.current, text)
        rebuilt = P.fill_images(rebuild(lesson, self.text), P.images(self.live))
        self.exact = json.dumps(loose(P.normalized(P.trimmed(rebuilt))), sort_keys=True) == \
            json.dumps(loose(P.normalized(self.live)), sort_keys=True)

    @property
    def differs(self) -> bool:
        return self.text != self.current

    def lines_changed(self) -> int:
        return sum(1 for d in difflib.unified_diff(self.current.splitlines(), self.text.splitlines(), lineterm="", n=0)
                   if d[:1] in "+-" and not d.startswith(("+++", "---")))

    def show(self) -> None:
        print(P.paint("1", f"\n{P.key(self.lesson)}"))
        for d in difflib.unified_diff(self.current.splitlines(), self.text.splitlines(), "repo", "site", lineterm="", n=1):
            color = "32" if d.startswith("+") else "31" if d.startswith("-") else "36" if d.startswith("@@") else "2"
            print(P.paint(color, d))
        for w in dict.fromkeys(self.warnings):
            print(P.paint("1;31", f"WARNING: {w}"))
        if not self.exact:
            print(P.paint("33", "Note: this doesn't match the site exactly, so publishing later might change a few small things on the page."))

    def save(self) -> None:
        (self.lesson / "lecture.md").write_text(self.text, encoding="utf-8")
        P.remember(self.act, self.live)
        print(P.paint("32", f"saved {P.key(self.lesson)}/lecture.md"))


def ask(question: str) -> bool:
    sys.path.insert(0, str(P.ROOT / "tools"))
    from ui import confirm
    return confirm(question)


SITE_KINDS = {"SUBTYPE_DYNAMIC_EMBED": "embed", "SUBTYPE_DYNAMIC_MARKDOWN": "markdown",
              "SUBTYPE_DYNAMIC_PAGE": "page", "TYPE_ASSIGNMENT": "assignment"}


def site_only(api: P.Api, folders: list[Path]) -> list[str]:
    """Pages on the site that aren't in the repo (made by hand, like Credits or an embed), in the
    courses or chapters being checked. Publishing leaves these where they are."""
    known = {v for sec in ("lessons", "homework", "checkins") for v in (P.IDS.get(sec) or {}).values()}
    courses: dict[str, set | None] = {}   # course folder -> chapter ids to look in (None = all)
    for f in folders:
        parts = P.key(f).split("/") if f != P.COURSES else []
        if len(parts) > 2:
            continue   # a single lesson
        for c in ([parts[0]] if parts else list(P.IDS.get("courses") or {})):
            if len(parts) == 2:
                ch = (P.IDS.get("chapters") or {}).get("/".join(parts))
                if courses.get(c, set()) is not None:
                    courses.setdefault(c, set()).add(ch)
            else:
                courses[c] = None
    lines = []
    for c, chapters in courses.items():
        cid = (P.IDS.get("courses") or {}).get(c)
        if not cid:
            continue
        meta = api.get(f"/courses/course_{cid}/meta?with_unpublished_activities=true&slim=true") or {}
        for ch in meta.get("chapters") or []:
            if chapters is not None and ch.get("id") not in chapters:
                continue
            for a in ch.get("activities") or []:
                uid = a["activity_uuid"].removeprefix("activity_")
                if uid in known:
                    continue
                kind = SITE_KINDS.get(a.get("activity_sub_type")) or SITE_KINDS.get(a.get("activity_type")) or "page"
                url = ""
                if kind in ("embed", "markdown"):
                    content = (api.get(f"/activities/{a['activity_uuid']}") or {}).get("content") or {}
                    url = content.get("embed_url") or content.get("markdown_url") or ""
                where = f"{c}  /  {ch.get('name')}  /  {a.get('name')}"
                lines.append(f"  {where}  {P.paint('2', f'({kind}' + (f': {url}' if url else '') + ')')}")
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="*", type=Path, help="courses, chapters or lessons to check (asks if left out)")
    ap.add_argument("-y", "--yes", action="store_true", help="pull every changed page without asking")
    args = ap.parse_args()
    sys.path.insert(0, str(P.ROOT / "tools"))
    import ui

    folders = [f.resolve() for f in args.folders]
    if not folders:
        if not sys.stdin.isatty():
            folders = [P.COURSES]
        else:
            items = outline()
            everything = "Everything"
            pick = ui.search("What should I check for changes on the site?", [everything] + [label for label, _ in items])
            if not pick:
                print("cancelled")
                return 0
            folders = [P.COURSES] if pick == everything else [dict(items)[pick]]
    for f in folders:
        if P.COURSES != f and P.COURSES not in f.parents:
            sys.exit(f"not under courses/: {f}")

    # One lesson named on its own: always show how it compares, even if the site looks unchanged.
    named = len(folders) == 1 and (folders[0] / "lecture.md").exists()
    lessons = list(dict.fromkeys(le for f in folders for le in lessons_under(f)))
    if not lessons:
        print("nothing in there is on the site yet")
        return 0

    api = P.Api(P.token())
    changed: list[Pulled] = []
    with P.Spinner("Checking the site...") as spin:
        for le in lessons:
            spin.update(f"Checking {P.key(le)}...")
            act = (P.IDS.get("lessons") or {}).get(P.key(le))
            if not named:
                live = P.trimmed((api.get(f"/activities/activity_{act}") or {}).get("content") or {})
                if not P.edited_on_site(act, live):
                    continue
            page = Pulled(api, le)
            if not page.differs:
                # Saved in the editor but nothing that matters changed: count it as published.
                if page.exact:
                    P.remember(page.act, page.live)
                continue
            changed.append(page)
            spin.echo(f"{P.paint('33', 'changed')}  {P.key(le)}  ({page.lines_changed()} line(s))")

    if not named:
        with P.Spinner("Looking for pages that are only on the site..."):
            extra = site_only(api, folders)
        if extra:
            print(P.paint("2", "Only on the site (not in the repo, so there's nothing to pull; publishing leaves them alone):"))
            for line in extra:
                print(line)
    if not changed:
        print(P.paint("2", "lecture.md already matches the site." if named else "nothing changed on the site"))
        return 0
    print(P.paint("2", f"{len(changed)} page(s) changed on the site"))

    if args.yes:
        picked = changed
    elif not sys.stdin.isatty():
        sys.exit("not saving without confirmation (run it in a terminal, or use -y)")
    elif len(changed) == 1:
        picked = changed
    else:
        labels = {P.key(c.lesson): c for c in changed}
        picked = [labels[k] for k in ui.pick_many("Which pages do you want to pull?", list(labels))]
        if not picked:
            print("nothing pulled")
            return 0

    saved = 0
    for page in picked:
        page.show()
        if args.yes or ask(f"Save this into {P.key(page.lesson)}/lecture.md?"):
            page.save()
            saved += 1
        else:
            print(P.paint("2", "skipped"))
    print(P.paint("2", f"pulled {saved} of {len(picked)}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
