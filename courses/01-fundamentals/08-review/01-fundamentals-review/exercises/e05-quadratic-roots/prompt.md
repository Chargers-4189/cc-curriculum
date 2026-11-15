---
title: "Quadratic Roots"
type: homework
difficulty: medium
---

The roots of `ax² + bx + c = 0` are:

```
x = (-b ± √(b² - 4ac)) / 2a
```

Ask for `a`, `b`, and `c`, then print both roots. If `b² - 4ac` is negative, there are no real roots, so print `No real roots` instead.

```
Enter a, b, c: 4 -8 1
Roots: 1.8660254037844386 and 0.1339745962155614
```

```
Enter a, b, c: 1 0 1
No real roots
```

Print the `+` root first.

**Hints:**
- `Math.sqrt(x)` gives the square root of `x`.
- Calculate `b² - 4ac` once and store it in a variable (it's called the **discriminant**).
- Watch your parentheses! `/ 2 * a` is not the same as `/ (2 * a)`.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get quadratic-roots
cd quadratic-roots
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
