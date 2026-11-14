## Motivation

- "Last time `1 / 0` crashed the program. How could we stop that?" → decision points
- Flowchart slide: condition → true path / false path → rejoin

## if, else, else if

- Basic if: `if (true)` vs `if (false)`; show the skipped print
- Circle area: reject radius ≤ 0 (the "retype radius" else)
- Driving example with `age = 22`: ask what prints, run it, then ask why "rent a car" never shows
  - First true branch wins; reorder most-specific first
- Spell out the rules: else if = previous false AND this true; else = none were true

## Nested Ifs

- Entry / ID example nested, then flattened with `&&`
- Neither is "right"; pick the readable one

## Guards

- Short-circuit with `divisor != 0 && ...`
- Decimals with a threshold (callback to relational operators)

## Traps (demo each live)

- No braces: indentation lies, only the next line is in the if
- Stray semicolon after the condition
- `if (x = 5)` won't compile
- Habit: always use braces

## Optional

- Ternary `? :` for short value choices
- Dangling else (one more argument for braces)

## Practice

- Subtraction Quiz: random numbers with `Math.random()`, swap so the answer isn't negative, Scanner for the answer
