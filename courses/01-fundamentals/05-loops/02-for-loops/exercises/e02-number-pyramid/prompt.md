---
title: "Number Pyramid (Homework)"
---

# Number Pyramid (Homework)

## Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get number-pyramid
cd number-pyramid
ccm test        # check your work
```

## Task

Write a program, `NumberPyramid.java`, that prompts for a number of lines from 1 to 15 and prints a number pyramid:

```
Enter the number of lines: 5
            1
         2  1  2
      3  2  1  2  3
   4  3  2  1  2  3  4
5  4  3  2  1  2  3  4  5
```

Build it in pieces rather than all at once:

1. Print just the **descending** half of each row (`5 4 3 2 1`).
2. Add the **ascending** half (`2 3 4 5`).
3. Add the **leading spaces** so it centers.

Each row needs **three** inner loops (spaces, counting down, counting up), and the bounds of each one depend on the row number.

**Requirements:**
- Read the number of lines with a `Scanner`.
- Print row `n` as the numbers `n n-1 ... 1 ... n-1 n`, one row per line.

**Hint:** `System.out.printf("%3d", number)` prints a number in a space 3 characters wide, which keeps two-digit numbers lined up.

Run `ccm test` to check your work. The tests check the numbers in each row, not the exact spacing.
