---
title: "Subtraction Quiz"
type: homework
difficulty: medium
---

Write a program for a 1st grader to practice subtraction.

1. Randomly generate two single-digit integers, `num1` and `num2`.
2. Make sure `num1` is not smaller than `num2` (so the answer isn't negative). If it is, **swap** them.
3. Ask the student the question, like `What is 9 - 2? `
4. Read their answer and say whether it's correct. If it's wrong, show the right answer.

```
What is 7 - 3? 4
You are correct!
```

```
What is 8 - 5? 2
Your answer is wrong.
8 - 5 is 3
```

**Hints:**
- `(int) (Math.random() * 10)` gives a random integer from 0 to 9.
- Swapping needs a third variable: `int temp = num1; num1 = num2; num2 = temp;`
- Since the numbers are random, run it several times. Try a right answer **and** a wrong one.

*Adapted from Listing 3.3 in Introduction to Java Programming (Liang).*

## In Labs

Download it and write your code in `Main.java`:

```bash
ccm get subtraction-quiz
cd subtraction-quiz
```

There are no automatic tests for this one (the numbers are random), so run it a few times yourself and make sure every path works. Then copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
