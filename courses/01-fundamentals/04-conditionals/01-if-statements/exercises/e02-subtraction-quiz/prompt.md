---
title: "Subtraction Quiz"
---

# Subtraction Quiz

## Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get subtraction-quiz
cd subtraction-quiz
```

## Task

Develop a program for a 1st grader to practice subtraction.

1. Randomly generate two single-digit integers, `num1` and `num2`.
2. Make sure `num1` is not smaller than `num2` (so the answer isn't negative). If it is, swap them.
3. Prompt the student: `What is 9 - 2? `
4. Read their answer and report whether it is correct. If it's wrong, show the right answer.

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
