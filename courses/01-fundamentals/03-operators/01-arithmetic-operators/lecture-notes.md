---
title: "Arithmetic Operators"
---

# Arithmetic Operators - Lecture Notes

## Week 1 Review

- Run through the review slide quickly; call on people for each bullet

## Basic Operators

- Follow-along file: `a = 17, b = 5`; have them predict each line before running
- `/` gives 3, not 3.4; let that surprise them, then explain
- `%` = remainder; long division picture: 17 ÷ 5 = 3 R 2
- Uses of `%`: even/odd, last digit, wrapping (days of the week; they'll need this for Review)

## Integer vs Floating-point Division

- Rule: both ints → int division; either double → decimal
- `3 / 4` is 0; ask "how do I get 0.75?" → make one side a double
- Integer divide by zero crashes; show the exception

## Overflow

- `Integer.MAX_VALUE + 1` → -2147483648
- Odometer analogy: rolls back around; no error, which is what makes it dangerous

## ++ and --

- `j++` uses then adds; `++j` adds then uses
- Work `l++ + ++l` on the board: 5 + 7 = 12, l ends at 7
- Advice: keep `++` on its own line

## Compound Assignment

- `+=`, `*=`, `/=`; show `count` going 10 → 13 → 130 → 13

## String Concatenation

- `1 + 2` vs `1 + 2 + "3"` vs `"1" + 2 + 3`; predict first
- Left to right; once it's a String, everything after is joined

## Order of Operations

- PEMDAS-like; parentheses win
- Full precedence chart comes in the next lesson with relational and logical operators
