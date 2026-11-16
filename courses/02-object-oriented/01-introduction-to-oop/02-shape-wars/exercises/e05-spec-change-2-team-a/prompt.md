---
title: "Spec Change 2: Team A"
type: practice
difficulty: easy
---

You're on **Team A**. Here's the spec change:

> **Spec Change 2**
> That's not how the amoeba is supposed to rotate. The others spin around their center. The amoeba spins around a point at **one end**, like a clock hand. The amoeba's rotation point is (0, 10).

After the square, circle and triangle, your program should also print:

```
--- user clicked the amoeba ---
Rotating the amoeba 360 degrees around (0.0, 10.0)
Playing amoeba.mp3
```

This starts from Team A's code after Spec Change 1. `rotate(int shapeNum)` works out the center from the width and height. Where can the amoeba's point go?

Count how many lines of code that already worked you had to change. That's your score, and lower is better.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get spec-change-2-team-a
cd spec-change-2-team-a
ccm test
```
