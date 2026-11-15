#!/usr/bin/env python3
"""Check curriculum structure, exercise front matter, quizzes, practice sets and links.

    python tools/validate/validate.py            # errors fail, warnings don't
    python tools/validate/validate.py --strict   # warnings fail too (used for releases)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from cases import read_cases, render_junit  # noqa: E402
COURSES = ROOT / "courses"

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
NUM_DIR = re.compile(rf"^(\d{{2}})-({SLUG})$")
EX_DIR = re.compile(rf"^e(\d{{2}})-({SLUG})$")

REQUIRED_LESSON_FILES = ["lecture.md"]  # lecture-notes.md, reading.md, slides.md are optional
LESSON_MD = {"lecture.md", "lecture-notes.md", "reading.md"}  # published to the LMS: no front matter

QUESTION_FIELDS = {  # type -> (required fields, optional fields)
    "mc":          ({"question", "answer", "incorrect"}, set()),
    "tf":          ({"question", "answer"}, set()),
    "short":       ({"question", "answer"}, set()),
    "long":        ({"question"}, {"answer"}),
    "code-output": ({"question", "code", "answer"}, {"incorrect"}),
    "flashcard":   ({"front", "back"}, set()),
}
COMMON_OPTIONAL = {"type", "points", "explanation", "tags"}
QUIZ_TYPES = set(QUESTION_FIELDS) - {"flashcard"}
PRACTICE_TYPES = set(QUESTION_FIELDS)
SET_KEYS = ({"title", "questions"}, {"description"})

# LearnHouse callout blocks, written as GitHub-style alerts: "> [!TIP]" on its own line
CALLOUT_TYPES = {"INFO", "TIP", "WARNING", "SUCCESS", "ERROR"}
CALLOUT_ALIASES = {"NOTE": "INFO", "IMPORTANT": "WARNING", "CAUTION": "ERROR"}
CALLOUT = re.compile(r"^(>?)\s*\[!(\w+)\](.*)$", re.M)

EXERCISE_TYPES = {"follow-along", "practice", "homework"}  # practice = code playground, homework = assignment
DIFFICULTIES = {"easy", "medium", "hard"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"ERROR {rel(path)}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"WARN  {rel(path)}: {msg}")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def num(name: str) -> int:
    return int(name.split("-", 1)[0].lstrip("e"))


def slug(name: str) -> str:
    return name.split("-", 1)[1]


def address(path: Path) -> str:
    parts = []
    for seg in path.relative_to(COURSES).parts:
        if seg == "exercises":
            continue
        parts.append(f"e{num(seg)}" if EX_DIR.match(seg) else str(num(seg)))
    return ".".join(parts)


# ---------------------------------------------------------------- helpers ---

def load_yaml(path: Path, r: Report):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        r.error(path, f"invalid YAML: {e}")
        return None
    return data


def front_matter(path: Path, r: Report) -> tuple[dict | None, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        r.error(path, "missing front matter (file must start with ---)")
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        r.error(path, "front matter is not closed with ---")
        return None, text
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as e:
        r.error(path, f"invalid front matter YAML: {e}")
        return None, text
    if not isinstance(data, dict):
        r.error(path, "front matter must be key: value pairs")
        return None, text
    return data, text[end + 4:]


def strip_code(body: str) -> str:
    return re.sub(r"^(```|~~~).*?^\1", "", body, flags=re.S | re.M)


def headings(body: str) -> list[tuple[int, str]]:
    out = []
    for m in re.finditer(r"^(#{1,6})\s+(.*?)\s*#*\s*$", strip_code(body), re.M):
        out.append((len(m.group(1)), m.group(2).strip().lower()))
    return out


def check_title(path: Path, fm: dict | None, r: Report) -> None:
    if fm is None:
        return
    title = fm.get("title")
    if not isinstance(title, str):
        r.error(path, "front matter needs a 'title'")
    elif not title.strip():
        r.warn(path, "title is empty")


LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


def check_links(path: Path, body: str, r: Report) -> None:
    for m in LINK.finditer(re.sub(r"<!--.*?-->", "", strip_code(body), flags=re.S)):
        target = m.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target and not (path.parent / target).exists():
            r.error(path, f"broken link: {target}")


def check_callouts(path: Path, body: str, r: Report) -> None:
    for m in CALLOUT.finditer(strip_code(body)):
        quote, kind, rest = m.group(1), m.group(2), m.group(3).strip()
        if kind not in CALLOUT_TYPES:
            hint = f"; use [!{CALLOUT_ALIASES[kind]}]" if kind in CALLOUT_ALIASES else ""
            r.error(path, f"unknown callout [!{kind}] (LearnHouse has {', '.join(sorted(CALLOUT_TYPES))}){hint}")
        elif not quote:
            r.error(path, f"callout [!{kind}] must start a blockquote: '> [!{kind}]'")
        elif rest:
            r.error(path, f"put the callout text on the next line ('> ...'), not after [!{kind}]")


# ---------------------------------------------------------- question sets ---

def check_question_set(path: Path, allowed: set[str], r: Report) -> None:
    data = load_yaml(path, r)
    if data is None:
        return
    if not isinstance(data, dict):
        r.error(path, "must be a mapping with 'title' and 'questions'")
        return
    required, optional = SET_KEYS
    for k in required - data.keys():
        r.error(path, f"missing '{k}'")
    for k in data.keys() - required - optional:
        r.error(path, f"unknown key '{k}'")
    if isinstance(data.get("title"), str) and not data["title"].strip():
        r.warn(path, "title is empty")
    qs = data.get("questions")
    if not isinstance(qs, list) or not qs:
        r.error(path, "'questions' must be a non-empty list")
        return
    for i, q in enumerate(qs, 1):
        where = f"question {i}"
        if not isinstance(q, dict):
            r.error(path, f"{where}: must be a mapping")
            continue
        qtype = q.get("type")
        if qtype not in allowed:
            r.error(path, f"{where}: type must be one of {', '.join(sorted(allowed))} (got {qtype!r})")
            continue
        req, opt = QUESTION_FIELDS[qtype]
        for k in sorted(req - q.keys()):
            r.error(path, f"{where} ({qtype}): missing '{k}'")
        for k in sorted(q.keys() - req - opt - COMMON_OPTIONAL):
            r.error(path, f"{where} ({qtype}): unknown key '{k}'")
        for k in ("question", "front", "back", "code", "explanation"):
            if k in q and not isinstance(q[k], str):
                r.error(path, f"{where}: '{k}' must be text")
            elif k in q and not q[k].strip():
                r.warn(path, f"{where}: '{k}' is empty")
        if "points" in q and (isinstance(q["points"], bool) or not isinstance(q["points"], (int, float))):
            r.error(path, f"{where}: 'points' must be a number")
        if "tags" in q and not (isinstance(q["tags"], list) and all(isinstance(t, str) for t in q["tags"])):
            r.error(path, f"{where}: 'tags' must be a list of text")
        if "answer" in q:
            a = q["answer"]
            if qtype == "tf":
                if not isinstance(a, bool):
                    r.error(path, f"{where}: tf answer must be true or false")
            elif isinstance(a, bool) or not isinstance(a, (str, int, float)) or a is None:
                r.error(path, f"{where}: answer must be text or a number")
            elif str(a).strip() == "":
                r.warn(path, f"{where}: answer is empty")
        if "incorrect" in q:
            inc = q["incorrect"]
            if not isinstance(inc, list) or not all(isinstance(x, (str, int, float)) and not isinstance(x, bool) for x in inc):
                r.error(path, f"{where}: 'incorrect' must be a list of answers")
            else:
                if qtype == "mc" and not inc:
                    r.error(path, f"{where}: mc needs at least one incorrect answer")
                if any(str(x).strip() == "" for x in inc):
                    r.warn(path, f"{where}: an incorrect answer is empty")
                if "answer" in q and str(q["answer"]) in {str(x) for x in inc} and str(q["answer"]).strip():
                    r.error(path, f"{where}: the correct answer is also listed as incorrect")
                if len({str(x) for x in inc}) != len(inc) and all(str(x).strip() for x in inc):
                    r.error(path, f"{where}: duplicate incorrect answers")


def check_csv_quiz(path: Path, r: Report) -> None:
    """quiz/*.csv: question,answer[,answer_2,...],incorrect_1,... (becomes an Interactive Quiz on the LMS)."""
    import csv
    import io
    rows = list(csv.reader(io.StringIO(path.read_text(encoding="utf-8"))))
    head = [c.strip() for c in rows[0]] if rows else []
    extra = [c for c in head[2:] if c.startswith("answer_")]
    if head[:2] != ["question", "answer"] or head[2:2 + len(extra)] != extra or \
            not all(c.startswith("incorrect") for c in head[2 + len(extra):]) or len(head) < 3 + len(extra):
        r.error(path, "header must be: question,answer[,answer_2,...],incorrect_1,incorrect_2,...")
        return
    n_right = 2 + len(extra)
    if len(rows) < 2:
        r.error(path, "no questions")
    seen = set()
    for i, row in enumerate(rows[1:], 2):
        where = f"line {i}"
        if len(row) != len(rows[0]):
            r.error(path, f"{where}: has {len(row)} columns, the header has {len(rows[0])}")
            continue
        q, a = row[0].strip(), row[1].strip()
        right = [a] + [x.strip() for x in row[2:n_right] if x.strip()]
        wrong = [x.strip() for x in row[n_right:] if x.strip()]
        if not q or not a:
            r.error(path, f"{where}: question and answer can't be empty")
        if "\n" in row[0]:
            r.error(path, f"{where}: the LMS shows questions on one line; remove the line breaks")
        if not wrong:
            r.error(path, f"{where}: needs at least one incorrect answer")
        if set(right) & set(wrong):
            r.error(path, f"{where}: a correct answer is also listed as incorrect")
        if len(set(right)) != len(right):
            r.error(path, f"{where}: duplicate correct answers")
        if len(set(wrong)) != len(wrong):
            r.error(path, f"{where}: duplicate incorrect answers")
        if q in seen:
            r.error(path, f"{where}: duplicate question")
        seen.add(q)


CHECKIN_TASKS = {
    "quiz": ({"type", "questions"}, {"title", "points", "description", "hint"}),
    "number": ({"type", "prompt", "answer"}, {"title", "points", "tolerance", "unit", "explanation", "description", "hint"}),
    "short": ({"type", "prompt", "answers"}, {"title", "points", "match", "explanation", "description", "hint"}),
    "fill-in": ({"type", "questions"}, {"title", "points", "description", "hint"}),
}


def check_checkin(path: Path, course: Path, r: Report) -> None:
    """courses/<course>/check-ins/*.yaml: a graded assignment with several tasks."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        r.error(path, f"invalid YAML: {e}")
        return
    for k in ("title", "after", "tasks"):
        if not data.get(k):
            r.error(path, f"needs '{k}'")
    for k in data.keys() - {"title", "after", "description", "tasks"}:
        r.error(path, f"unknown key '{k}'")
    after = data.get("after")
    if isinstance(after, str) and not (course / after / "lecture.md").exists():
        r.error(path, f"after: no lesson at {course.name}/{after}")
    for i, t in enumerate(data.get("tasks") or [], 1):
        where = f"task {i}"
        kind = t.get("type") if isinstance(t, dict) else None
        if kind not in CHECKIN_TASKS:
            r.error(path, f"{where}: type must be one of {', '.join(CHECKIN_TASKS)}")
            continue
        need, opt = CHECKIN_TASKS[kind]
        for k in need - t.keys():
            r.error(path, f"{where}: needs '{k}'")
        for k in t.keys() - need - opt:
            r.error(path, f"{where}: unknown key '{k}'")
        if kind == "number" and not isinstance(t.get("answer"), (int, float)):
            r.error(path, f"{where}: answer must be a number")
        if kind == "short" and not t.get("answers"):
            r.error(path, f"{where}: needs at least one accepted answer")
        for j, q in enumerate(t.get("questions") or [], 1):
            qw = f"{where}, question {j}"
            if kind == "quiz":
                right = q.get("answers") or ([q["answer"]] if "answer" in q else [])
                wrong = q.get("incorrect") or []
                if not q.get("question") or not right or not wrong:
                    r.error(path, f"{qw}: needs question, answer (or answers), and incorrect")
                if set(map(str, right)) & set(map(str, wrong)):
                    r.error(path, f"{qw}: a correct answer is also listed as incorrect")
            elif not q.get("text") or not q.get("blanks") or not all("answer" in b for b in q["blanks"]):
                r.error(path, f"{qw}: needs text and blanks, each with an answer")


# -------------------------------------------------------------- structure ---

def numbered_children(parent: Path, pattern: re.Pattern, kind: str, r: Report,
                      allowed_other: set[str]) -> list[Path]:
    kids, seen = [], {}
    for p in sorted(parent.iterdir()):
        if p.name.startswith("."):
            continue
        if p.is_dir() and pattern.match(p.name):
            n = num(p.name)
            if n in seen:
                r.error(p, f"{kind} number {p.name.split('-')[0]} is also used by {seen[n]}")
            seen[n] = p.name
            kids.append(p)
        elif p.name not in allowed_other:
            hint = f" ({kind} folders must look like 01-name)" if p.is_dir() else ""
            r.error(p, f"unexpected {'folder' if p.is_dir() else 'file'}{hint}")
    return kids


def check_meta_yaml(path: Path, allowed: set[str], r: Report) -> dict:
    if not path.is_file():
        r.error(path, "missing")
        return {}
    data = load_yaml(path, r) or {}
    if not isinstance(data, dict):
        r.error(path, "must be key: value pairs")
        return {}
    if not isinstance(data.get("title"), str):
        r.error(path, "needs a 'title'")
    elif not data["title"].strip():
        r.warn(path, "title is empty")
    for k in data.keys() - allowed:
        r.error(path, f"unknown key '{k}'")
    return data


def validate(r: Report) -> None:
    lesson_names: dict[str, Path] = {}
    exercise_names: dict[str, Path] = {}

    if not COURSES.is_dir():
        r.error(COURSES, "missing courses/ folder")
        return

    for course in numbered_children(COURSES, NUM_DIR, "course", r, set()):
        meta = check_meta_yaml(course / "course.yaml", {"title", "description", "slides", "includes"}, r)
        if "slides" in meta and not isinstance(meta["slides"], bool):
            r.error(course / "course.yaml", "'slides' must be true or false")
        for inc in meta.get("includes") or []:
            if not isinstance(inc, str) or ".." in inc or inc.startswith("/") or not (ROOT / inc).exists():
                r.error(course / "course.yaml", f"include not found: {inc}")
        has_slides = meta.get("slides") is True

        for f in sorted((course / "check-ins").glob("*")) if (course / "check-ins").is_dir() else []:
            if f.suffix == ".yaml":
                check_checkin(f, course, r)
            else:
                r.error(f, "check-ins/ only holds .yaml files")

        for chapter in numbered_children(course, NUM_DIR, "chapter", r, {"course.yaml", "check-ins"}):
            check_meta_yaml(chapter / "chapter.yaml", {"title", "description"}, r)

            for lesson in numbered_children(chapter, NUM_DIR, "lesson", r, {"chapter.yaml"}):
                name = slug(lesson.name)
                if name in lesson_names:
                    r.error(lesson, f"lesson name '{name}' is also used by {rel(lesson_names[name])}")
                lesson_names.setdefault(name, lesson)

                for f in REQUIRED_LESSON_FILES:
                    if not (lesson / f).is_file():
                        r.error(lesson, f"missing {f}")
                if (lesson / "slides.md").is_file() and not has_slides:
                    r.warn(lesson / "slides.md", "course.yaml doesn't set 'slides: true'")

                for md in sorted(lesson.rglob("*.md")):
                    if "exercises" in md.relative_to(lesson).parts:
                        continue
                    body = md.read_text(encoding="utf-8")
                    if md.name in LESSON_MD and body.startswith("---\n"):
                        r.error(md, "lesson files have no front matter (the LMS shows the title)")
                    check_links(md, body, r)
                    check_callouts(md, body, r)

                if (lesson / "quiz").is_dir():
                    quiz_files = sorted((lesson / "quiz").glob("*.y*ml"))
                    csv_files = sorted((lesson / "quiz").glob("*.csv"))
                    if not quiz_files and not csv_files:
                        r.warn(lesson / "quiz", "no quiz .csv or .yaml files")
                    for qf in quiz_files:
                        check_question_set(qf, QUIZ_TYPES, r)
                    for qf in csv_files:
                        check_csv_quiz(qf, r)
                if (lesson / "practice").is_dir():
                    for pf in sorted((lesson / "practice").glob("*.y*ml")):
                        check_question_set(pf, PRACTICE_TYPES, r)

                ex_root = lesson / "exercises"
                if ex_root.is_dir():
                    for ex in numbered_children(ex_root, EX_DIR, "exercise", r, set()):
                        check_exercise(ex, exercise_names, r)

    # ccm finds things by bare name, so one name on two different things is ambiguous.
    # (lesson/lesson and exercise/exercise clashes are already reported above)
    named: dict[str, tuple[str, Path]] = {}
    kinds = [("course", "[0-9]*-*"), ("chapter", "[0-9]*-*/[0-9]*-*"),
             ("lesson", "[0-9]*-*/[0-9]*-*/[0-9]*-*"), ("exercise", "[0-9]*-*/[0-9]*-*/[0-9]*-*/exercises/e[0-9]*-*")]
    for kind, pattern in kinds:
        for item in sorted(p for p in COURSES.glob(pattern) if p.is_dir()):
            name = slug(item.name)
            if name in named:
                other_kind, other = named[name]
                if not (kind == other_kind and kind in ("lesson", "exercise")):
                    r.error(item, f"name '{name}' is also used by the {other_kind} {rel(other)}; "
                                  f"`ccm get {name}` would be ambiguous")
            else:
                named[name] = (kind, item)



def check_exercise(ex: Path, names: dict[str, Path], r: Report) -> None:
    name = slug(ex.name)
    if name in names:
        r.error(ex, f"exercise name '{name}' is also used by {rel(names[name])} (exercise names must be unique)")
    names.setdefault(name, ex)
    prompt = ex / "prompt.md"
    if not prompt.is_file():
        r.error(ex, "missing prompt.md")
    else:
        fm, body = front_matter(prompt, r)
        check_title(prompt, fm, r)
        check_links(prompt, body, r)
        check_callouts(prompt, body, r)
        if fm is not None:
            check_exercise_type(ex, prompt, fm, r)
    for p in ex.iterdir():
        if p.name.startswith(".") or p.name == "prompt.md":
            continue
        if p.name not in {"starter", "tests", "solution"}:
            r.warn(p, "exercise folders normally contain only prompt.md, starter/, tests/, solution/")
    tests = ex / "tests"
    if tests.is_dir():
        if not any(tests.rglob("*.java")):
            r.error(tests, "no .java test files")
        if not (ex / "solution").is_dir():
            r.warn(ex, "has tests/ but no solution/ (CI can't check the tests)")


def check_exercise_type(ex: Path, prompt: Path, fm: dict, r: Report) -> None:
    kind = fm.get("type")
    if kind is None:
        return
    if kind not in EXERCISE_TYPES:
        r.error(prompt, f"type must be one of {', '.join(sorted(EXERCISE_TYPES))} (got {kind!r})")
        return
    if kind == "follow-along":
        return
    # practice and homework run on the LMS, which always runs Main.java
    for d in ("starter", "solution"):
        if not (ex / d / "Main.java").is_file():
            r.error(ex / d, f"{kind} exercises need {d}/Main.java (the LMS code editor runs Main.java)")
    if fm.get("difficulty") not in DIFFICULTIES:
        r.error(prompt, f"difficulty must be one of {', '.join(sorted(DIFFICULTIES))}")
    cases = ex / "tests" / "cases.csv"
    if not cases.is_file():
        if kind == "practice":
            r.error(ex, "practice exercises need tests/cases.csv")
        return
    try:
        read_cases(cases)
    except ValueError as e:
        r.error(cases, str(e))
        return
    test = ex / "tests" / "MainTest.java"
    if not test.is_file() or test.read_text(encoding="utf-8") != render_junit(cases):
        r.error(test, "out of date with cases.csv; run python3 tools/cases.py")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    r = Report()
    validate(r)
    for line in r.errors + r.warnings:
        print(line)
    failed = bool(r.errors) or (args.strict and bool(r.warnings))
    print(f"\n{len(r.errors)} error(s), {len(r.warnings)} warning(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
