#!/usr/bin/env python3
"""Turn each exercise's tests/cases.csv into tests/MainTest.java.

cases.csv is the one place a playground exercise's tests live. The same rows become
the Charging Courses code playground's test cases (tools/lms/build.py) and the JUnit
tests that `ccm test` runs in Labs, so the two always agree.

    label,input,output,hidden
    "Doubles 4","4","8",
    "Negative","-3","-6",yes

- input   what the user types (each line is one Enter)
- output  everything the program prints, prompts included. Spaces at the end of a line
          and blank lines at the end don't matter; everything else must match.
- hidden  optional; "yes" hides the case from students on homework assignments

    python3 tools/cases.py            # regenerate every MainTest.java
    python3 tools/cases.py --check    # fail if any MainTest.java is out of date (CI)
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLUMNS = ["label", "input", "output", "hidden"]


def read_cases(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rows = list(csv.DictReader(io.StringIO(text)))
    cases = []
    for i, row in enumerate(rows, 1):
        missing = [c for c in ("label", "input", "output") if c not in row]
        if missing:
            raise ValueError(f"{path}: needs columns {', '.join(COLUMNS[:3])} (row {i} is missing {missing})")
        stdin = row["input"].replace("\r\n", "\n")
        if stdin and not stdin.endswith("\n"):
            stdin += "\n"
        cases.append({
            "label": row["label"].strip() or f"Test {i}",
            "input": stdin,
            "output": row["output"].replace("\r\n", "\n"),
            "hidden": (row.get("hidden") or "").strip().lower() in {"yes", "y", "true", "1"},
        })
    if not cases:
        raise ValueError(f"{path}: no test cases")
    return cases


def java_string(s: str) -> str:
    out = []
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\t":
            out.append("\\t")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


def render_junit(csv_path: Path) -> str:
    cases = read_cases(csv_path)
    lines = [
        "// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.",
        "import org.junit.jupiter.api.DisplayName;",
        "import org.junit.jupiter.api.Test;",
        "",
        "class MainTest {",
    ]
    for i, c in enumerate(cases, 1):
        lines += [
            "    @Test",
            f"    @DisplayName({java_string(c['label'])})",
            f"    void case{i}() {{",
            f"        TestUtil.assertOutput(Main.class, {java_string(c['input'])}, {java_string(c['output'])});",
            "    }",
            "",
        ]
    lines[-1] = "}"
    return "\n".join(lines) + "\n"


def case_files() -> list[Path]:
    return sorted(ROOT.glob("courses/*/*/*/exercises/*/tests/cases.csv"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="only report out-of-date files")
    args = ap.parse_args()
    stale = 0
    for csv_path in case_files():
        target = csv_path.parent / "MainTest.java"
        want = render_junit(csv_path)
        have = target.read_text(encoding="utf-8") if target.exists() else None
        if have == want:
            continue
        stale += 1
        if args.check:
            print(f"out of date: {target.relative_to(ROOT)} (run python3 tools/cases.py)")
        else:
            target.write_text(want, encoding="utf-8")
            print(f"wrote {target.relative_to(ROOT)}")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
