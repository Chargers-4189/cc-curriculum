---
title: "Spec Change 1: Team B"
type: practice
difficulty: easy
---

You're on **Team B**. Here's the spec change:

> **Spec Change 1**
> There will be an amoeba shape on the screen with the others. When the user clicks it, it rotates like the others and plays an **.mp3** sound file instead of a .wav. The amoeba is 35 wide and 20 tall.

After the square, circle and triangle, your program should also print:

```
--- user clicked the amoeba ---
Rotating the amoeba 360 degrees around (17.5, 10.0)
Playing amoeba.mp3
```

Team B has a class for each shape. A new shape can be a new class at the bottom of the file (no `public`), plus the lines in `main` that click it.

Count how many lines of code that already worked you had to change. That's your score, and lower is better.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get spec-change-1-team-b
cd spec-change-1-team-b
ccm test
```
