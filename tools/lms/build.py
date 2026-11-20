#!/usr/bin/env python3
"""Build Charging Courses (LearnHouse) page content from a lesson's markdown.

Turns lecture.md into the editor's document format (TipTap/ProseMirror JSON), and swaps in
the interactive pieces:

  [Quiz](quiz/review.csv)                  a paragraph that is only a link to a quiz CSV
                                           -> an Interactive Quiz block (answer_2... columns
                                              make a select-all-that-apply question)
  [Title](exercises/e02-x/prompt.md)       a paragraph that is only a link to a practice exercise
                                           -> a Code Playground (starter, solution, tests from cases.csv)
                                           a homework exercise -> a link to its assignment page
  [Lesson](../x/lecture.md#heading)        -> the lesson's page on Charging Courses
  > [!TIP] ...                             -> a callout block
  {{user.first_name}}                      -> a dynamic variable (shows the student's own info);
  {{user.full_name|capitalize|there}}         optional |format|fallback
  [General](community:community_<uuid>)    -> a tag linking to that community

Images can't be uploaded from here, so each image becomes a placeholder that the upload script
fills with the image block already on that page (in order).

    python3 tools/lms/build.py courses/01-fundamentals/02-java-basics/02-hello-world -o out/
    python3 tools/lms/build.py --homework courses/.../exercises/e05-day-of-week -o out/

Page and assignment ids live in tools/lms/ids.yaml.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import random
import re
import sys
import uuid
from pathlib import Path

try:
    import yaml
    from markdown_it import MarkdownIt
except ModuleNotFoundError as e:
    sys.exit(f"Missing Python package: {e.name}. Install the tools' requirements first:\n"
             "    python3 -m pip install -r tools/requirements.txt")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from cases import read_cases  # noqa: E402

SITE = "https://chargingcourses.com"
NS = uuid.UUID("6f1c2b0e-4189-4189-4189-000000004189")
CALLOUT = re.compile(r"^\[!(INFO|TIP|WARNING|SUCCESS|ERROR)\]\s*$")
IDS_FILE = Path(__file__).parent / "ids.yaml"
IDS = yaml.safe_load(IDS_FILE.read_text(encoding="utf-8")) or {}


def sid(*parts: str) -> str:
    """A stable id. Paths count from the repo, so every clone (on any computer) gets the same ids."""
    root = str(ROOT) + "/"
    return str(uuid.uuid5(NS, "/".join(p[len(root):] if p.startswith(root) else p for p in parts)))


def front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        return yaml.safe_load(text[4:end]) or {}, text[end + 4:].lstrip("\n")
    return {}, text


def without_labs(body: str) -> str:
    """Drop the '## In Labs' section (the page shows its own ccm line)."""
    return re.split(r"^## In Labs\s*$", body, flags=re.M)[0].strip() + "\n"


def course_of(path: Path) -> str | None:
    """The Charging Courses course id for any file or folder inside courses/<course>/."""
    rel = path.resolve().relative_to(ROOT / "courses")
    return (IDS.get("courses") or {}).get(rel.parts[0])


def lesson_url(lesson: Path, anchor: str = "") -> str | None:
    key = str(lesson.relative_to(ROOT / "courses"))
    act = (IDS.get("lessons") or {}).get(key)
    course = course_of(lesson)
    if not act or not course:
        return None
    url = f"{SITE}/course/{course}/activity/{act}"
    return url + (f"#heading-{anchor}" if anchor else "")


def homework_url(ex: Path) -> str | None:
    act = (IDS.get("homework") or {}).get(ex.name.split("-", 1)[1])
    course = course_of(ex)
    return f"{SITE}/course/{course}/activity/{act}" if act and course else None


def reload_ids() -> None:
    """Re-read ids.yaml (after new pages were created)."""
    IDS.clear()
    IDS.update(yaml.safe_load(IDS_FILE.read_text(encoding="utf-8")) or {})


# ------------------------------------------------------------------ nodes ---

def text(t: str, marks: list | None = None) -> dict:
    n = {"type": "text", "text": t}
    if marks:
        n["marks"] = [dict(m) for m in marks]
    return n


VARIABLE = re.compile(r"\{\{\s*([\w.]+)\s*(?:\|\s*(\w*)\s*)?(?:\|\s*([^}]*?)\s*)?\}\}")


def with_variables(t: str, marks: list) -> list[dict]:
    """Text with {{user.first_name}} / {{user.full_name|capitalize|there}} (path|format|fallback)
    turned into the editor's dynamic variables, which show each student their own info."""
    out, pos = [], 0
    for m in VARIABLE.finditer(t):
        if m.start() > pos:
            out.append(text(t[pos:m.start()], marks))
        out.append({"type": "dynamicVariable", "attrs": {
            "path": m.group(1), "format": m.group(2) or None, "fallback": m.group(3) or ""}})
        pos = m.end()
    if pos < len(t):
        out.append(text(t[pos:], marks))
    return out


def para(*inline) -> dict:
    content = [i for i in inline if i]
    return {"type": "paragraph", "content": content} if content else {"type": "paragraph"}


def link_mark(href: str) -> dict:
    return {"type": "link", "attrs": {"href": href, "target": "_blank", "rel": "noopener noreferrer",
                                      "class": None, "title": None}}


class Builder:
    def __init__(self, lesson: Path):
        self.lesson = lesson
        self.images: list[str] = []
        self.warnings: list[str] = []
        self.md = MarkdownIt("commonmark").enable("table")

    # ---- links
    def resolve(self, href: str) -> str | None:
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            return href if not href.startswith("#") else f"#heading-{href[1:]}"
        path, _, anchor = href.partition("#")
        target = (self.lesson / path).resolve()
        if target.name == "lecture.md":
            url = lesson_url(target.parent, anchor)
            if url:
                return url
        elif target.name == "prompt.md" and target.parent.parent.name == "exercises":
            url = homework_url(target.parent)
            if url:
                return url
        self.warnings.append(f"no Charging Courses link for {href}; left as plain text")
        return None

    # ---- inline
    def inline(self, tokens) -> list[dict]:
        out, marks = [], []
        community = None  # [Name](community:<uuid>) being read
        for t in tokens:
            if community is not None and t.type != "link_close":
                community["name"] += t.content
                continue
            if t.type == "text":
                out.extend(with_variables(t.content, marks))
            elif t.type == "code_inline":
                out.append(text(t.content, marks + [{"type": "code"}]))
            elif t.type == "softbreak":
                out.append(text(" ", marks))
            elif t.type == "hardbreak":
                out.append({"type": "hardBreak"})
            elif t.type in ("strong_open", "em_open"):
                marks.append({"type": "bold" if t.type == "strong_open" else "italic"})
            elif t.type in ("strong_close", "em_close"):
                kind = "bold" if t.type == "strong_close" else "italic"
                for i in range(len(marks) - 1, -1, -1):
                    if marks[i]["type"] == kind:
                        marks.pop(i)
                        break
            elif t.type == "link_open" and t.attrGet("href").startswith("community:"):
                community = {"communityUuid": t.attrGet("href").split(":", 1)[1], "name": ""}
            elif t.type == "link_close" and community is not None:
                out.append({"type": "communityTag", "attrs": community})
                community = None
            elif t.type == "link_open":
                href = self.resolve(t.attrGet("href"))
                marks.append(link_mark(href) if href else {"type": "_nolink"})
            elif t.type == "link_close":
                for i in range(len(marks) - 1, -1, -1):
                    if marks[i]["type"] in ("link", "_nolink"):
                        marks.pop(i)
                        break
            elif t.type == "image":
                self.images.append(t.attrGet("src"))
                out.append({"type": "__image", "attrs": {"index": len(self.images) - 1, "src": t.attrGet("src")}})
            elif t.type == "html_inline":
                continue
            else:
                out.append(text(t.content, marks))
        # drop the placeholder mark used for unresolved links and merge nothing else
        for n in out:
            if "marks" in n:
                n["marks"] = [m for m in n["marks"] if m["type"] != "_nolink"] or None
                if not n["marks"]:
                    del n["marks"]
        return out

    # ---- blocks
    def blocks(self, tokens, i: int = 0, stop: str | None = None) -> tuple[list[dict], int]:
        out = []
        while i < len(tokens):
            t = tokens[i]
            if stop and t.type == stop:
                return out, i + 1
            if t.type == "heading_open":
                inl = self.inline(tokens[i + 1].children)
                out.append({"type": "heading", "attrs": {"level": int(t.tag[1])}, "content": inl})
                i += 3
            elif t.type == "paragraph_open":
                children = tokens[i + 1].children
                special = self.special_paragraph(children)
                if special is not None:
                    out.extend(special)
                else:
                    inl = self.inline(children)
                    imgs = [n for n in inl if n["type"] == "__image"]
                    if imgs and all(n["type"] == "__image" or (n["type"] == "text" and not n["text"].strip()) for n in inl):
                        out.extend(imgs)
                    else:
                        out.append(para(*inl))
                i += 3
            elif t.type == "fence" or t.type == "code_block":
                lang = (t.info or "").strip().split(" ")[0] or None
                code = t.content.rstrip("\n")
                node = {"type": "codeBlock", "attrs": {"language": lang}}
                if code:
                    node["content"] = [text(code)]
                out.append(node)
                i += 1
            elif t.type in ("bullet_list_open", "ordered_list_open"):
                kind = "bulletList" if t.type == "bullet_list_open" else "orderedList"
                close = t.type.replace("_open", "_close")
                items, i = self.list_items(tokens, i + 1, close)
                node = {"type": kind, "content": items}
                if kind == "orderedList":
                    node["attrs"] = {"start": int(t.attrGet("start") or 1)}
                out.append(node)
            elif t.type == "blockquote_open":
                inner, i = self.blocks(tokens, i + 1, "blockquote_close")
                out.append(self.maybe_callout(inner))
            elif t.type == "table_open":
                rows, i = self.table(tokens, i + 1)
                out.append({"type": "table", "content": rows})
            elif t.type == "hr":
                out.append({"type": "horizontalRule"})
                i += 1
            elif t.type in ("html_block",):
                i += 1
            else:
                i += 1
        return out, i

    def list_items(self, tokens, i, close):
        items = []
        while tokens[i].type != close:
            if tokens[i].type == "list_item_open":
                content, i = self.blocks(tokens, i + 1, "list_item_close")
                items.append({"type": "listItem", "content": content or [para()]})
            else:
                i += 1
        return items, i + 1

    def table(self, tokens, i):
        rows = []
        cell_type = "tableCell"
        while tokens[i].type != "table_close":
            t = tokens[i]
            if t.type == "thead_open":
                cell_type = "tableHeader"
            elif t.type == "tbody_open":
                cell_type = "tableCell"
            elif t.type == "tr_open":
                cells = []
                i += 1
                while tokens[i].type != "tr_close":
                    if tokens[i].type in ("th_open", "td_open"):
                        inl = self.inline(tokens[i + 1].children)
                        cells.append({"type": cell_type, "attrs": {"colspan": 1, "rowspan": 1, "colwidth": None, "align": None},
                                      "content": [para(*inl)]})
                        i += 3
                    else:
                        i += 1
                rows.append({"type": "tableRow", "content": cells})
            i += 1
        return rows, i + 1

    def maybe_callout(self, inner: list[dict]) -> dict:
        first = inner[0] if inner else None
        if first and first["type"] == "paragraph" and first.get("content"):
            head = first["content"][0]
            if head["type"] == "text":
                m = re.match(r"^\[!(INFO|TIP|WARNING|SUCCESS|ERROR)\]\s*", head["text"])
                if m:
                    rest = head["text"][m.end():]
                    first["content"] = ([text(rest, head.get("marks"))] if rest.strip() else []) + first["content"][1:]
                    if first["content"] and first["content"][0]["type"] == "text":
                        first["content"][0]["text"] = first["content"][0]["text"].lstrip()
                    if not first["content"]:
                        inner = inner[1:]
                    return {"type": "callout", "attrs": {"type": m.group(1).lower(), "dismissible": False},
                            "content": inner or [para()]}
        return {"type": "blockquote", "content": inner or [para()]}

    # ---- quiz / playground / homework links
    def special_paragraph(self, children) -> list[dict] | None:
        kids = [c for c in children if not (c.type == "text" and not c.content.strip()) and c.type != "softbreak"]
        if len(kids) < 3 or kids[0].type != "link_open" or kids[-1].type != "link_close":
            return None
        href = kids[0].attrGet("href")
        target = (self.lesson / href).resolve()
        if not re.match(r"^[a-z]+:", href) and not target.exists():
            self.warnings.append(f"broken link {href}: file not found")
            return None
        if target.suffix == ".csv" and target.parent.name == "quiz":
            return [quiz_block(target)]
        if target.name == "prompt.md" and target.parent.parent.name == "exercises":
            fm, _ = front_matter(target)
            kind = fm.get("type")
            if kind == "practice":
                return playground(target.parent)
            if kind == "homework":
                url = homework_url(target.parent)
                title = fm.get("title", target.parent.name)
                if not url:
                    self.warnings.append(f"homework {target.parent.name} has no assignment id yet")
                    return [para(text("Homework: "), text(title, [{"type": "bold"}]))]
                return [para(text("📝 Open the "), text(title, [{"type": "bold"}, link_mark(url)]),
                             text(" assignment"))]
        return None


def quiz_block(path: Path) -> dict:
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
    questions = []
    for row in rows:
        q = row["question"].strip()
        right = [row["answer"].strip()] + [
            row[k].strip() for k in sorted(row) if k.startswith("answer_") and row[k] and row[k].strip()]
        answers = [(a, True) for a in right] + [
            (row[k].strip(), False) for k in sorted(row) if k.startswith("incorrect") and row[k] and row[k].strip()]
        random.Random(q).shuffle(answers)
        questions.append({
            "question_id": sid(str(path), q),
            "question": q,
            "type": "multiple_choice",
            "response_type": "multiple" if len(right) > 1 else "single",
            "answers": [{"answer_id": sid(str(path), q, a), "answer": a, "correct": ok} for a, ok in answers],
        })
    return {"type": "blockQuiz", "attrs": {"quizId": None, "questions": questions}}


def exercise_parts(ex: Path) -> dict:
    fm, body = front_matter(ex / "prompt.md")
    cases = read_cases(ex / "tests" / "cases.csv") if (ex / "tests" / "cases.csv").exists() else []
    return {
        "name": ex.name.split("-", 1)[1],
        "title": fm.get("title", ex.name),
        "type": fm.get("type"),
        "difficulty": fm.get("difficulty", "easy"),
        "description": without_labs(body),
        "starter": (ex / "starter" / "Main.java").read_text(encoding="utf-8"),
        "solution": (ex / "solution" / "Main.java").read_text(encoding="utf-8"),
        "cases": cases,
    }


def playground(ex: Path) -> list[dict]:
    p = exercise_parts(ex)
    attrs = {
        "mode": "advanced", "languageId": 62, "languageName": "Java",
        "starterCode": p["starter"],
        "testCases": [{"id": sid(str(ex), c["label"]), "label": c["label"], "stdin": c["input"],
                       "expectedStdout": c["output"]} for c in p["cases"]],
        "description": p["description"], "hints": [], "difficulty": p["difficulty"],
        "solutionCode": p["solution"], "maxAttemptsBeforeReveal": 5,
        "timeComplexity": "", "spaceComplexity": "", "timeLimitMs": 10000,
        "sqliteDbPath": "", "sqliteDbName": "", "timedMode": False, "timedDurationMs": 300000,
        "additionalFiles": [],
    }
    return [{"type": "blockCode", "attrs": attrs},
            para(text("In Labs: "), text(f"ccm get {p['name']}", [{"type": "code"}]))]


def clean(node: dict) -> dict:
    """Remove empty text nodes (the editor rejects them) and merge neighbours with the same marks."""
    if "content" in node:
        merged = []
        for child in node["content"]:
            child = clean(child)
            if child["type"] == "text" and child["text"] == "":
                continue
            prev = merged[-1] if merged else None
            if prev and prev["type"] == "text" and child["type"] == "text" and prev.get("marks") == child.get("marks"):
                prev["text"] += child["text"]
            else:
                merged.append(child)
        node["content"] = merged
        if not merged and node["type"] == "paragraph":
            del node["content"]
    return node


def build_lesson(lesson: Path) -> dict:
    b = Builder(lesson)
    tokens = b.md.parse((lesson / "lecture.md").read_text(encoding="utf-8"))
    content, _ = b.blocks(tokens)
    content = [clean(n) for n in content]
    return {"lesson": str(lesson.relative_to(ROOT)), "activity": (IDS.get("lessons") or {}).get(
        str(lesson.relative_to(ROOT / "courses"))), "images": b.images, "warnings": b.warnings,
        "content": {"type": "doc", "content": content}}


# Assignment descriptions are shown as plain text (line breaks kept, no markdown), so homework
# instructions are written plain and the prompt is converted with plain_text().
HOMEWORK_INTRO = """HOW TO DO THIS HOMEWORK
Write your code below and click Run Tests. To use Labs instead, run ccm get {name}, check it with ccm test, and paste all of Main.java here.
Click Hand in my work when you're done.{note}

THE TASK
"""

TASK_LINE = "Write your program here (keep the class named Main), then click Run Tests."


def plain_text(md: str) -> str:
    """Markdown -> readable plain text for places the LMS doesn't render markdown."""
    def inline(line: str) -> str:
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        line = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", line)  # *italic*
        line = re.sub(r"`([^`]+)`", r"\1", line)
        return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)

    def table(rows: list[str]) -> list[str]:
        """A markdown table as a list: "- first cell: other cells". The header row is dropped,
        since the page isn't monospace and columns wouldn't line up."""
        cells = [[inline(c.strip()) for c in r.strip().strip("|").split("|")] for r in rows]
        body = [r for r in cells[2:]] if len(cells) > 2 and re.fullmatch(r"\|?[\s:|-]+\|?", rows[1].strip()) else cells
        return ["- " + r[0] + (": " + "; ".join(c for c in r[1:] if c) if any(r[1:]) else "") for r in body]

    out, in_code, rows = [], False, []
    for line in md.strip("\n").split("\n") + [""]:
        if rows and not line.lstrip().startswith("|"):
            out += table(rows)
            rows = []
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            out.append("    " + line)
            continue
        if line.lstrip().startswith("|"):
            rows.append(line)
            continue
        out.append(inline(re.sub(r"^#{1,6}\s+", "", line)))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def build_homework(ex: Path) -> dict:
    p = exercise_parts(ex)
    hidden = any(c["hidden"] for c in p["cases"])
    note = "\nSome tests are hidden." if hidden else ""
    if not p["cases"]:
        note = "\nThere are no automatic tests because the numbers are random. Run it a few times and try every path."
    return {
        "name": p["name"], "title": p["title"],
        "assignment_description": HOMEWORK_INTRO.format(name=p["name"], note=note) + plain_text(p["description"]),
        "task": {
            "title": p["title"], "description": TASK_LINE, "hint": "",
            "assignment_type": "CODE", "max_grade_value": 100,
            "contents": {
                "language_id": 62, "starter_code": p["starter"], "solution_code": p["solution"],
                "grading_mode": "equal_weight",
                "test_cases": [{"id": "tc_" + sid(str(ex), c["label"]), "label": c["label"], "stdin": c["input"],
                                "expectedStdout": c["output"], "hidden": c["hidden"], "weight": 1} for c in p["cases"]],
                "allow_student_run": True, "show_test_details_on_fail": True, "show_hidden_test_count": True,
                "require_passing_to_submit": False, "show_solution_after_submit": False,
            },
        },
    }


# ---------------------------------------------------------------- check-ins ---
# A check-in is a graded assignment made of several tasks, written as one YAML file in
# courses/<course>/check-ins/. Task types:
#   quiz     questions with `answer` (or `answers` for select-all-that-apply) and `incorrect`
#   number   `prompt` and a numeric `answer` (optional `tolerance`, `unit`)
#   short    `prompt` and accepted `answers` (matched ignoring case)
#   fill-in  `questions`, each with `text` and `blanks` (each blank has `answer`, optional `hint`)
# Every task can have `points` (default 10 per question / blank / answer).

TASK_TYPES = {"quiz": "QUIZ", "number": "NUMBER_ANSWER", "short": "SHORT_ANSWER", "fill-in": "FORM"}


def read_checkin(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def checkin_task(path: Path, i: int, t: dict) -> dict:
    kind = t["type"]
    base = f"check-in:{path.parent.parent.name}/{path.stem}#{i}"  # stays the same if folders move
    if kind == "quiz":
        questions = []
        for q in t["questions"]:
            right = [str(a) for a in (q.get("answers") or [q["answer"]])]
            opts = [(a, True) for a in right] + [(str(a), False) for a in q.get("incorrect") or []]
            random.Random(q["question"]).shuffle(opts)
            questions.append({
                "questionText": q["question"], "questionUUID": "question_" + sid(base, q["question"]),
                "response_type": "multiple" if len(right) > 1 else "single",
                "options": [{"optionUUID": "option_" + sid(base, q["question"], a), "text": a, "fileID": "",
                             "type": "text", "assigned_right_answer": ok} for a, ok in opts]})
        contents = {"questions": questions, "grading_mode": "all_or_nothing"}
        points = t.get("points", 10 * len(questions))
    elif kind == "number":
        contents = {"prompt": t["prompt"], "correct_value": t["answer"], "tolerance": t.get("tolerance", 0),
                    "unit": t.get("unit", ""), "explanation": t.get("explanation", "")}
        points = t.get("points", 10)
    elif kind == "short":
        contents = {"prompt": t["prompt"], "correct_answers": [str(a) for a in t["answers"]],
                    "match_mode": t.get("match", "case_insensitive"), "explanation": t.get("explanation", "")}
        points = t.get("points", 10)
    elif kind == "fill-in":
        questions = []
        for q in t["questions"]:
            questions.append({
                "questionText": q["text"], "questionUUID": "question_" + sid(base, q["text"]),
                "blanks": [{"blankUUID": "blank_" + sid(base, q["text"], str(j)), "placeholder": b.get("hint", "answer"),
                            "correctAnswer": str(b["answer"]), "hint": ""} for j, b in enumerate(q["blanks"])]})
        contents = {"questions": questions}
        points = t.get("points", 10 * sum(len(q["blanks"]) for q in t["questions"]))
    else:
        raise ValueError(f"{path}: unknown task type {kind!r}")
    return {"title": t.get("title") or t.get("prompt") or kind, "description": t.get("description", ""),
            "hint": t.get("hint", ""), "assignment_type": TASK_TYPES[kind], "contents": contents,
            "max_grade_value": points}


def build_checkin(path: Path) -> dict:
    c = read_checkin(path)
    return {"title": c["title"], "after": c["after"],
            "assignment_description": c.get("description", "").strip() + "\n",
            "tasks": [checkin_task(path, i, t) for i, t in enumerate(c["tasks"])]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--homework", action="store_true", help="paths are homework exercise folders")
    ap.add_argument("-o", "--out", type=Path, required=True)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for p in args.paths:
        p = p.resolve()
        data = build_homework(p) if args.homework else build_lesson(p)
        name = (p.name.split("-", 1)[1] if args.homework else p.name)
        (args.out / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        for w in data.get("warnings", []):
            print(f"warning: {p.name}: {w}", file=sys.stderr)
        print(f"wrote {args.out / (name + '.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
