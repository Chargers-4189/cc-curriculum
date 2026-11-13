---
title: "While Loops"
---

# While Loops - Lecture Notes

## Motivation

- "Print Welcome to Java 100 times": copy-paste is tedious and error-prone
- Loops repeat a block while a condition is true

## while Basics

- Syntax and flow: check → body → check again
- Sum 1..9 example; trace `i` and `sum` on the board for the first few passes
- The two things every loop needs: something that changes + a condition that becomes false
- Delete `i++` to show an infinite loop; Ctrl + C to stop it

## 3-Step Recipe

- Do it once → wrap in `while (true)` → real condition
- Students freeze trying to write the whole loop at once; the recipe fixes that

## Sentinel Loops

- When you don't know the count, the user decides
- 0 means "done", not data
- Read before the loop AND at the bottom
- If the first input is 0, the body never runs

## Guess the Number (build it live with the recipe)

- Step 1: one guess and compare
- Step 2: `while (true)`, which never ends
- Step 3: `guess != number`
- Why `guess = -1`: 0 is a valid secret number
- Optional strategy tie-in: always guess the middle (binary search)

## Optional: do-while

- Body first, condition after: runs at least once
- Removes the duplicated read from the sentinel loop
- Needs the semicolon after `while (...)`
