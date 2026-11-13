---
title: "Conditionals (Follow Along)"
---

# Conditionals (Follow Along)

## Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get conditional-demo
cd conditional-demo
```

## Task

Follow along with the lecture in `Conditional.java`.

1. Write an `if` / `else if` / `else` that prints whether someone can drive (16+) or rent a car (21+). Test it with `age = 22`. Is the output what you expected? Why?
2. **Circle area:** calculate the area of a circle (`area = 3.14 * r * r`). Don't accept a radius of 0 or below; print a message instead.
3. Rewrite the nested "entry allowed / ID required" check as a single `if` / `else if` using `&&`.
4. Find the bugs: an `if` with no braces, and an `if` with a stray semicolon. What prints, and why?
5. Use `&&` to safely check `dividend / divisor == 2` when `divisor` might be 0.
6. Compare `0.1 + 0.2` to `0.3` with `==`, then the right way.
