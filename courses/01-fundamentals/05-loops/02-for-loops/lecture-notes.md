---
title: "For Loops"
---

# For Loops - Lecture Notes

## From while to for

- Show the counting while loop; point at the three scattered parts
- Same loop as a for: all three in the header, so you can't forget the update
- Default choice when you know the count

## Order of Execution

- Walk through slowly: init once → condition → body → update → condition...
- Trace `for (int k = 0; k < 3; k++)` on the board
- The header variable dies with the loop (try printing `k` after; it won't compile)

## Counting

- Countdown with `k--`; steps with `k += 5`
- Off-by-one: `<` vs `<=`

## Which Loop

- for: known count; while: unknown count

## Nested Loops

- Outer = rows, inner = columns
- Multiplication table; 81 printfs
- Move the `println()` into the inner loop on purpose and let them see one long column
- `printf("%4d")` for alignment
- Cost: nesting multiplies

## break / continue

- break: leave now (stop at sum ≥ 100 → 105)
- continue: skip this pass (sum of odds → 100)
- break in nested loops only exits the inner loop

## Homework

- Number Pyramid: three inner loops per row (spaces, down, up); build it in pieces
- Leap Years: divisible by 4 but not 100, or by 400; 10 per line with a counter; don't forget the newline before the total
- Both have tests: `ccm test`
