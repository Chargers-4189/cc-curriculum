#!/usr/bin/env python3
"""Check curriculum structure, front matter, quizzes, practice sets and links.

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
COURSES = ROOT / "courses"

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
NUM_DIR = re.compile(rf"^(\d{{2}})-({SLUG})$")
EX_DIR = re.compile(rf"^e(\d{{2}})-({SLUG})$")
ADDRESS = re.compile(r"^\d+\.\d+\.\d+$")

REQUIRED_LESSON_FILES = ["lecture.md", "lecture-notes.md", "reading.md"]
SECTIONED_FILES = ["lecture.md", "reading.md"]  # must contain the required sections

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


def check_sections(path: Path, body: str, r: Report) -> None:
    hs = headings(body)
    h2 = [t for lvl, t in hs if lvl == 2]
    h3 = [t for lvl, t in hs if lvl == 3]
    if "objectives" not in h2:
        r.error(path, "missing '## Objectives' section")
    if "prerequisites" not in h2:
        r.error(path, "missing '## Prerequisites' section")
    if not any("review" in t or "conclusion" in t for t in h2):
        r.error(path, "missing '## Review' (or '## Conclusion') section")
    if "readings" not in h2:
        r.error(path, "missing '## Readings' section")
    else:
        for sub in ("required", "further"):
            if sub not in h3:
                r.error(path, f"missing '### {sub.title()}' under Readings")


LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


def check_links(path: Path, body: str, r: Report) -> None:
    for m in LINK.finditer(re.sub(r"<!--.*?-->", "", strip_code(body), flags=re.S)):
        target = m.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target and not (path.parent / target).exists():
            r.error(path, f"broken link: {target}")


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
    prereqs: list[tuple[Path, str]] = []
    lessons: list[Path] = []

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

        for chapter in numbered_children(course, NUM_DIR, "chapter", r, {"course.yaml"}):
            check_meta_yaml(chapter / "chapter.yaml", {"title", "description"}, r)

            for lesson in numbered_children(chapter, NUM_DIR, "lesson", r, {"chapter.yaml"}):
                lessons.append(lesson)
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
                    if md.name in ("lecture.md", "lecture-notes.md", "reading.md"):
                        fm, body = front_matter(md, r)
                        check_title(md, fm, r)
                        if md.name in SECTIONED_FILES:
                            check_sections(md, body, r)
                            pr = (fm or {}).get("prerequisites", [])
                            if fm is not None and "prerequisites" not in fm:
                                r.error(md, "front matter needs 'prerequisites' (use [] for none)")
                            elif not isinstance(pr, list) or not all(isinstance(x, (str, int, float)) for x in pr):
                                r.error(md, "'prerequisites' must be a list of lesson names or addresses")
                            else:
                                prereqs.extend((md, str(x)) for x in pr)
                    else:
                        body = md.read_text(encoding="utf-8")
                    check_links(md, body, r)

                if (lesson / "quiz").is_dir():
                    quiz_files = sorted((lesson / "quiz").glob("*.y*ml"))
                    if not quiz_files:
                        r.warn(lesson / "quiz", "no quiz .yaml files")
                    for qf in quiz_files:
                        check_question_set(qf, QUIZ_TYPES, r)
                if (lesson / "practice").is_dir():
                    for pf in sorted((lesson / "practice").glob("*.y*ml")):
                        check_question_set(pf, PRACTICE_TYPES, r)

                ex_root = lesson / "exercises"
                if ex_root.is_dir():
                    for ex in numbered_children(ex_root, EX_DIR, "exercise", r, set()):
                        check_exercise(ex, exercise_names, r)

    # prerequisites must point at real lessons
    by_addr = {address(l): l for l in lessons}
    for md, pre in prereqs:
        if ADDRESS.match(pre):
            normalized = ".".join(str(int(p)) for p in pre.split("."))
            if normalized not in by_addr:
                r.error(md, f"prerequisite {pre} is not a lesson")
        elif pre not in lesson_names:
            r.error(md, f"prerequisite '{pre}' is not a lesson name")


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
