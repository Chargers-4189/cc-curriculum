#!/usr/bin/env python3
"""Import a course from the Charging Courses LMS (Frappe LMS) into courses/ as Markdown.

    python tools/import/lms_import.py start-here-navigating-charging-courses courses/00-start-here
    python tools/import/lms_import.py <course-slug> <course dir> --force   # overwrite existing lessons

For each LMS chapter/lesson it creates NN-chapter/NN-lesson/ with:
  lecture.md        the lesson content converted to Markdown
  lecture-notes.md  instructor notes from the LMS, only if there are any
  assets/           images and files hosted on the LMS, downloaded

Only lessons the LMS shows publicly (preview) can be read without logging in; others are
created as placeholders.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "shared" / "templates"
DEFAULT_BASE = "https://chargingcourses.com"
UA = {"User-Agent": "cc-curriculum-importer"}


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()


def api(base: str, method: str, **params) -> object:
    url = f"{base}/api/method/{method}?{urllib.parse.urlencode(params)}"
    return json.loads(fetch(url)).get("message")


def slugify(title: str) -> str:
    s = title.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "untitled"


def yaml_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


# ------------------------------------------------------------ conversion ---

def inline(text: str) -> str:
    """Editor.js inline HTML -> Markdown."""
    t = re.sub(r"\s+", " ", text or "")   # HTML whitespace/newlines are just spaces
    t = re.sub(r"<br\s*/?>", "  \n", t, flags=re.I)
    t = re.sub(r'<a\s[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
               lambda m: f"[{m.group(2)}]({html.unescape(m.group(1))})", t, flags=re.I | re.S)
    t = re.sub(r"</?(b|strong)>", "**", t, flags=re.I)
    t = re.sub(r"</?(i|em)>", "*", t, flags=re.I)
    t = re.sub(r"</?code[^>]*>", "`", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)          # mark, u, span, etc.
    t = html.unescape(t).replace(" ", " ")
    return t.strip()


class Converter:
    def __init__(self, base: str, assets: Path):
        self.base = base
        self.assets = assets
        self.downloaded: list[str] = []
        self.failed: list[str] = []

    def local_file(self, url: str) -> str | None:
        """Download LMS-hosted files into assets/; returns relative path or None for external URLs."""
        if url.startswith("/"):
            url = self.base + url
        if not url.startswith(self.base):
            return None
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        src = q.get("file_url", [urllib.parse.urlparse(url).path])[0]
        name = re.sub(r"[^A-Za-z0-9._-]+", "_", Path(src).name) or "file"
        dest = self.assets / name
        if not dest.exists():
            try:
                data = fetch(url)
            except Exception as e:  # noqa: BLE001
                self.failed.append(f"{url} ({e})")
                return None
            self.assets.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            self.downloaded.append(name)
        return f"assets/{name}"

    def list_items(self, items: list, ordered: bool, depth: int = 0) -> list[str]:
        out = []
        for i, it in enumerate(items, 1):
            content = it.get("content", "") if isinstance(it, dict) else str(it)
            bullet = f"{i}." if ordered else "-"
            out.append(f"{'   ' * depth}{bullet} {inline(content)}")
            if isinstance(it, dict) and it.get("items"):
                out += self.list_items(it["items"], ordered, depth + 1)
        return out

    def block(self, b: dict) -> str | None:
        t, d = b.get("type"), b.get("data", {})
        if t == "header":
            level = min(int(d.get("level", 2)) + 2, 6)  # nested under "## Content"
            return f"{'#' * level} {inline(d.get('text', ''))}"
        if t == "paragraph":
            return inline(d.get("text", "")) or None
        if t == "markdown":
            text = html.unescape(d.get("text") or "").replace("\u00a0", " ")
            return text.strip() or None
        if t == "list":
            return "\n".join(self.list_items(d.get("items", []), d.get("style") == "ordered"))
        if t == "image":
            url = d.get("url") or d.get("file", {}).get("url", "")
            alt = inline(d.get("caption", "")) or "image"
            return f"![{alt}]({self.local_file(url) or url})"
        if t == "upload":
            url = d.get("file_url", "")
            path = self.local_file(url) or (self.base + url if url.startswith("/") else url)
            name = Path(urllib.parse.unquote(path)).name
            if (d.get("file_type") or "").upper() in {"JPG", "JPEG", "PNG", "GIF", "WEBP", "SVG", "IMAGE"}:
                return f"![{name}]({path})"
            return f"[{name}]({path})"
        if t == "code":
            return f"```\n{d.get('code', '').rstrip()}\n```"
        if t == "quote":
            return "\n".join(f"> {line}" for line in inline(d.get("text", "")).splitlines())
        if t == "embed":
            return f"[{d.get('service', 'Embedded content')}]({d.get('source') or d.get('embed')})"
        if t == "delimiter":
            return "---"
        if t == "table":
            rows = d.get("content", [])
            if not rows:
                return None
            fmt = lambda r: "| " + " | ".join(inline(c) for c in r) + " |"
            return "\n".join([fmt(rows[0]), "|" + "---|" * len(rows[0])] + [fmt(r) for r in rows[1:]])
        return f"<!-- unconverted LMS block ({t}): {json.dumps(d)[:300]} -->"

    def blocks(self, content: str | None) -> str:
        if not content:
            return ""
        try:
            blocks = json.loads(content).get("blocks", [])
        except (json.JSONDecodeError, AttributeError):
            return content.strip()  # plain markdown/HTML lesson
        parts = [p for p in (self.block(b) for b in blocks) if p]
        return "\n\n".join(parts)


# --------------------------------------------------------------- writing ---

def lecture_md(title: str, source: str, body: str) -> str:
    body = body.strip() or "<!-- This lesson's content requires an LMS login and was not imported. -->"
    return f"""---
title: {yaml_str(title)}
lms_source: {source}
---

# {title}

## Content

{body}
"""


def from_template(name: str, title: str) -> str:
    text = (TEMPLATES / "lesson" / name).read_text(encoding="utf-8")
    return text.replace('title: ""', f"title: {yaml_str(title)}", 1)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("course", help="LMS course slug (from the course URL)")
    ap.add_argument("dest", help="course folder in this repo, e.g. courses/00-start-here")
    ap.add_argument("--base", default=DEFAULT_BASE)
    ap.add_argument("--force", action="store_true", help="overwrite lessons that already exist")
    args = ap.parse_args()

    dest = Path(args.dest)
    if not (dest / "course.yaml").is_file():
        print(f"{dest}/course.yaml not found; create the course first (ccm new course <name>)", file=sys.stderr)
        return 1

    outline = api(args.base, "lms.lms.utils.get_course_outline", course=args.course) or []
    if not outline:
        print("course outline is empty or not public", file=sys.stderr)
        return 1

    problems = []
    for ch in outline:
        ch_dir = dest / f"{int(ch['idx']):02d}-{slugify(ch['title'])}"
        ch_dir.mkdir(parents=True, exist_ok=True)
        (ch_dir / "chapter.yaml").write_text(f'title: {yaml_str(ch["title"])}\ndescription: ""\n', encoding="utf-8")
        print(f"{ch_dir}")
        for les in ch["lessons"]:
            c_num, l_num = (int(x) for x in les["number"].split("-"))
            l_dir = ch_dir / f"{l_num:02d}-{slugify(les['title'])}"
            if l_dir.exists() and not args.force:
                print(f"  skip {l_dir.name} (exists; use --force)")
                continue
            data = api(args.base, "lms.lms.utils.get_lesson", course=args.course, chapter=c_num, lesson=l_num) or {}
            title = data.get("title") or les["title"]
            source = f"{args.base}/lms/courses/{args.course}/learn/{c_num}-{l_num}"
            conv = Converter(args.base, l_dir / "assets")
            body = conv.blocks(data.get("content")) or (data.get("body") or "")
            l_dir.mkdir(parents=True, exist_ok=True)
            (l_dir / "lecture.md").write_text(lecture_md(title, source, body), encoding="utf-8")
            notes = conv.blocks(data.get("instructor_content")) or (data.get("instructor_notes") or "").strip()
            if notes:
                notes_md = from_template("lecture-notes.md", title).split("\n## ", 1)[0].rstrip()
                (l_dir / "lecture-notes.md").write_text(notes_md + "\n\n" + notes + "\n", encoding="utf-8")
            status = "imported" if body.strip() else "PLACEHOLDER (needs login)"
            if data.get("no_preview") or not body.strip():
                problems.append(f"{l_dir}: content not public; placeholder created")
            if les.get("icon") == "icon-quiz" or data.get("quiz_id"):
                problems.append(f"{l_dir}: LMS quiz lesson; add quiz/quiz.yaml by hand")
            problems += [f"{l_dir}: failed to download {f}" for f in conv.failed]
            extra = f", {len(conv.downloaded)} file(s)" if conv.downloaded else ""
            print(f"  {l_dir.name}: {status}{extra}")

    if problems:
        print("\nNeeds attention:")
        for p in problems:
            print(f"  - {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
