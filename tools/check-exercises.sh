#!/usr/bin/env bash
# CI: every exercise with tests/ must pass them using its solution/.
# Starters that don't compile are reported as warnings (some are fill-in-the-blank).
set -euo pipefail
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
ccm="$root/tools/ccm"
status=0 checked=0
for ex in "$root"/courses/*/*/*/exercises/e*/; do
  [ -d "$ex" ] || continue
  ex=${ex%/}; rel=${ex#"$root"/}
  if [ -d "$ex/tests" ]; then
    if [ -d "$ex/solution" ]; then
      checked=$((checked + 1))
      "$ccm" _test-dir "$ex/solution" "$ex/tests" || status=1
    else
      echo "::warning file=$rel::has tests/ but no solution/; skipped"
    fi
  fi
  if [ -d "$ex/starter" ] && [ -n "$(find "$ex/starter" -name '*.java' -print -quit)" ]; then
    "$ccm" _compile-dir "$ex/starter" >/dev/null 2>&1 || echo "::warning file=$rel/starter::starter code does not compile"
  fi
done
echo "checked $checked exercise(s) with tests"
exit "$status"
