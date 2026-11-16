---
title: "Fix the Constructors"
type: practice
difficulty: easy
---

This doesn't compile. `main` is fine, so don't change it. Fix the `Pet` class so `main` works:

1. `Pet` is supposed to have a constructor that takes a name and an age, but something about it makes it a method instead. What is it?
2. `main` also does `new Pet()`. Add a no-arg constructor that names the pet `Unknown` with age `0`.

```
Unknown is 0 years old
Biscuit is 3 years old
```

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get fix-the-constructors
cd fix-the-constructors
ccm test
```
