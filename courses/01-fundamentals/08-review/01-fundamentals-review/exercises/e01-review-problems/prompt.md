---
title: "Review Problems"
---

# Review Problems

## Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get review-problems
cd review-problems
```

## Task

Solve these with what you've learned so far. They're in `Review.java` with `TODO`s.

### 1. 50 Days From Friday

If today is Friday, what day of the week will it be in 50 days? Use Java arithmetic operators (`+ - * / %`) to calculate it.

**Hint:** start with the days of the week numbered 1 → 7, where 1 is Monday and 7 is Sunday. What does `%` do when you go past 7?

Make it work for any starting `day` and any `length`, not just Friday and 50.

### 2. Quadratic Roots

The roots of `ax² + bx + c = 0` are:

```
x = (-b ± √(b² - 4ac)) / 2a
```

Calculate both roots for `a = 4`, `b = -8`, `c = 1`.

**Hints:**
- `Math.sqrt(x)` gives the square root of `x`.
- There are two roots: one with `+` and one with `-`.
- Watch your parentheses! `/ 2 * a` is not the same as `/ (2 * a)`.
- **Challenge:** if `b² - 4ac` is negative, there are no real roots. Print a message instead.
