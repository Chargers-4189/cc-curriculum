About 40 minutes. Every code example is a stop-and-ask: get an answer from the room before running it.

## Suggested Pacing

- 0:00 - 0:05  Variables and types
- 0:05 - 0:12  Arithmetic and operator traps
- 0:12 - 0:18  Booleans, conditions, if / else-if / switch
- 0:18 - 0:24  Loops
- 0:24 - 0:28  Arrays
- 0:28 - 0:35  Methods
- 0:35 - 0:40  One program that uses all of it + what to practice

## Variables

- Declaration vs initialization; casting truncates

## Arithmetic

- Predict: `17 / 5` vs `17.0 / 5`
- Overflow wraps silently
- `k++ + ++k`: work it on the board (12, 7)
- Concatenation order: `1 + 2 + "3"` vs `"1" + 2 + 3`

## Conditions

- Ladder order: write it backwards (`>= 70` first) and ask why every passing score gets a C
- Traps: `==` on Strings, stray semicolon, missing braces, missing break

## Loops

- Two things every loop needs
- for vs while
- Nested: how many lines and numbers does a 3x3 table print? (3 and 9)
- Off by one

## Arrays

- Index 0 to length - 1; loop pattern

## Methods

- Header as a contract; void vs returning
- Predict swap again; pass-by-value is the most-missed test question

## Putting It Together

- isPrime → countPrimesBelow; main reads like a summary
- Early return replaces break + flag

## Review Problems (the ??? in the notes)

- 50 days from Friday: `(day - 1 + length) % 7 + 1` → 6 (Saturday); explain the shift to 0-6 so % wraps
- Quadratic roots for a=4, b=-8, c=1: two roots (≈ 1.866, 0.134); `Math.sqrt`; parentheses around `2 * a`
