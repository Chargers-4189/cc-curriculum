#!/usr/bin/env python3
"""Export quiz/practice YAML into copy-paste-ready files.

For every lesson with quiz/*.csv, quiz/*.yaml or practice/*.yaml, writes to <out>/<address>-<lesson>/:
  quiz.md / practice.md      student version (options shuffled, no answers)
  quiz-key.md / practice-key.md   answer key with explanations
  flashcards.tsv             front<TAB>back, importable into Quizlet / Anki

    python tools/export/quiz.py                 # all lessons -> build/quizzes
    python tools/export/quiz.py 1.1.1 -o out    # one lesson (address prefix)
"""
from __future__ import annotations

import argparse
import csv
import io
import hashlib
import random
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "courses"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def num(seg: str) -> int:
    return int(seg.split("-", 1)[0].lstrip("e"))


def address(lesson: Path) -> str:
    return ".".join(str(num(s)) for s in lesson.relative_to(COURSES).parts)


def lessons() -> list[Path]:
    return sorted(p for p in COURSES.glob("[0-9]*-*/[0-9]*-*/[0-9]*-*") if p.is_dir())


def options(q: dict) -> list[str]:
    """Correct + incorrect answers, shuffled the same way every run."""
    opts = [str(x) for x in correct(q)] + [str(x) for x in q.get("incorrect") or []]
    seed = hashlib.sha256(str(q.get("question", "")).encode()).hexdigest()
    random.Random(seed).shuffle(opts)
    return opts


def correct(q: dict) -> list:
    """The right answer(s): `answer`, plus `also_correct` for select-all-that-apply questions."""
    return [q["answer"]] + list(q.get("also_correct") or [])


def code_block(code: str) -> list[str]:
    return ["", "```java", code.rstrip("\n"), "```"]


def render(data: dict, lesson: Path, key: bool) -> str:
    title = data.get("title") or "Quiz"
    out = [f"# {title}{' — Answer Key' if key else ''}", "", f"*{address(lesson)} {lesson.name.split('-', 1)[1]}*", ""]
    n = 0
    for q in data.get("questions") or []:
        t = q.get("type")
        if t == "flashcard":
            continue
        n += 1
        pts = f" *({q['points']} pt{'s' if q['points'] != 1 else ''})*" if "points" in q else ""
        many = (" *(select all that apply)*" if q.get("also_correct")
                and "select all" not in str(q.get("question", "")).lower() else "")
        out.append(f"**{n}.** {q.get('question', '').strip()}{many}{pts}")
        if t == "code-output":
            out += code_block(q.get("code", ""))
        out.append("")
        has_options = t == "mc" or (t == "code-output" and bool(q.get("incorrect")))
        if has_options:
            for i, opt in enumerate(options(q)):
                mark = "x" if key and opt in [str(x) for x in correct(q)] else " "
                out.append(f"- [{mark}] {LETTERS[i]}. {opt}")
        elif t == "tf":
            for opt in ("True", "False"):
                mark = "x" if key and (opt == "True") == bool(q["answer"]) else " "
                out.append(f"- [{mark}] {opt}")
        elif not key:
            out.append("Answer: ______________________" if t in ("short", "code-output") else "Answer:\n\n\n")
        if key:
            if t in ("short", "long", "code-output") and not has_options and q.get("answer") not in (None, ""):
                label = "Sample answer" if t == "long" else "Answer"
                out.append(f"**{label}:** {q['answer']}")
            if q.get("explanation"):
                out += ["", f"*{q['explanation'].strip()}*"]
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def flashcards(data: dict) -> list[str]:
    clean = lambda s: re.sub(r"\s+", " ", str(s)).strip()
    return [f"{clean(q['front'])}\t{clean(q['back'])}"
            for q in data.get("questions") or [] if q.get("type") == "flashcard"]


def load_csv_quiz(f: Path) -> dict:
    """quiz/*.csv: question,answer[,answer_2,...],incorrect_1,... -> the same shape as a YAML quiz."""
    rows = list(csv.DictReader(io.StringIO(f.read_text(encoding="utf-8"))))
    return {"title": f"{lesson_title(f.parent.parent)} Quiz", "questions": [
        {"type": "mc", "question": r["question"], "answer": r["answer"],
         "also_correct": [r[k] for k in sorted(r) if k.startswith("answer_") and r[k]],
         "incorrect": [r[k] for k in sorted(r) if k.startswith("incorrect") and r[k]]} for r in rows]}


def lesson_title(lesson: Path) -> str:
    return " ".join(w.capitalize() for w in lesson.name.split("-")[1:])


def export_lesson(lesson: Path, out_root: Path) -> int:
    written = 0
    dest = out_root / f"{address(lesson)}-{lesson.name.split('-', 1)[1]}"
    cards: list[str] = []
    for kind in ("quiz", "practice"):
        for f in sorted([*(lesson / kind).glob("*.y*ml"), *(lesson / kind).glob("*.csv")]):
            if f.suffix == ".csv":
                data = load_csv_quiz(f)
            else:
                data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
            stem = kind if f.stem == kind else f"{kind}-{f.stem}"
            dest.mkdir(parents=True, exist_ok=True)
            if any(q.get("type") != "flashcard" for q in data.get("questions") or []):
                (dest / f"{stem}.md").write_text(render(data, lesson, key=False), encoding="utf-8")
                (dest / f"{stem}-key.md").write_text(render(data, lesson, key=True), encoding="utf-8")
                written += 2
            cards += flashcards(data)
    if cards:
        (dest / "flashcards.tsv").write_text("\n".join(cards) + "\n", encoding="utf-8")
        written += 1
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("address", nargs="*", help="lesson/chapter/course address prefix, e.g. 1 or 1.2.1")
    ap.add_argument("-o", "--out", default=str(ROOT / "build" / "quizzes"))
    args = ap.parse_args()
    out = Path(args.out)
    total = 0
    for lesson in lessons():
        a = address(lesson)
        if args.address and not any(a == p or a.startswith(p + ".") for p in args.address):
            continue
        total += export_lesson(lesson, out)
    print(f"wrote {total} file(s) to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
