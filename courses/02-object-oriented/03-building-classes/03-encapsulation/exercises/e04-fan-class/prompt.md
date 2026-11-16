---
title: "Fan Class"
type: homework
difficulty: medium
---

`main` is already written, and the three speed constants are in your starter code. Write the rest of the `Fan` class. Every instance variable has to be **private**.

A `Fan` **knows**:

- `speed` (an `int`, `SLOW` by default)
- `on` (a `boolean`, `false` by default)
- `radius` (a `double`, `5` by default)
- `color` (a `String`, `"blue"` by default)

A `Fan` has:

- A **no-arg constructor** that makes a fan with all the defaults above
- A getter and setter for all four instance variables. The getter for `on` is `isOn()`
- `setSpeed` only changes the speed if it's `SLOW`, `MEDIUM` or `FAST`. Anything else is ignored
- `setRadius` only changes the radius if it's more than 0
- `describe()`, which **returns** a `String`:
  - If the fan is on: `speed <speed>, color <color>, radius <radius>`
  - If it's off: `color <color>, radius <radius>, fan is off`

When it works, the program prints:

```
speed 3, color yellow, radius 10.0
color blue, radius 5.0, fan is off
speed 2, color blue, radius 5.0
Is the first fan on? true
```

**Hints:**
- Build it one piece at a time: instance variables and the constructor first, then the getters and setters, then `describe()`.
- `describe()` returns the text, it doesn't print it. `main` does the printing.

*Adapted from Programming Exercise 9.8 in Introduction to Java Programming (Liang).*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get fan-class
cd fan-class
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
