---
title: "Robots in Methods and Arrays (Follow Along)"
type: follow-along
---

Follow along with the lesson in `ObjectsTester.java`. `Robot.java` is already done; you'll only use it. Each section of the lesson has a matching `// --- Section ---` comment, and the static methods go at the bottom of `ObjectsTester`.

1. Write `chargeUp(Robot r, int amount)` and see which one changes back in `main`.
2. Write `replace(Robot r)`, which points `r` at a new robot. Predict what `bolt` is afterward.
3. Write `makeSpare(String name)`, which makes and returns a new robot.
4. Make an array of three robots. Print a slot before you fill it.
5. Loop over the robots to find the average battery, first with a regular `for` loop and then with a for-each loop. Then write `lowest(Robot[] robots)`.

## In Labs

```bash
ccm get objects-demo
cd objects-demo
```

Run `ObjectsTester` with the Run button, or:

```bash
javac *.java
java ObjectsTester
```
