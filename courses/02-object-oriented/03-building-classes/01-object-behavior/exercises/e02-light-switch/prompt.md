---
title: "Light Switch"
type: practice
difficulty: easy
---

A `Light` knows if it's `on` and how bright it is. `main` is already written. Add two methods to `Light`:

- `toggle()` turns the light on if it's off, and off if it's on
- `describe()` prints `Light is on at <brightness>%` when it's on, and `Light is off` when it's off

```
Light is off
Light is on at 80%
Light is off
```

**Hint:** `on` starts as `false`. Each `toggle()` flips it. What does `!` do to a boolean?

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get light-switch
cd light-switch
ccm test
```
