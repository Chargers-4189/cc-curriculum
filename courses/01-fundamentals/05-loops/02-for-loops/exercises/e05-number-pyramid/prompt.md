---
title: "Number Pyramid"
type: homework
difficulty: hard
---

Ask for a number of lines from 1 to 15 and print a number pyramid:

```
Enter the number of lines: 5
              1
           2  1  2
        3  2  1  2  3
     4  3  2  1  2  3  4
  5  4  3  2  1  2  3  4  5
```

**Format:**
- Every number is printed with `System.out.printf("%3d", number)`, which takes up **3** spaces.
- Before the numbers, each row has **3 spaces for every number missing** on the left. Row 1 of 5 is missing 4, so it starts with 12 spaces.
- If the number is not from 1 to 15, print `The number of lines must be from 1 to 15` instead.

Build it in pieces:

1. Print just the **descending** half of each row (`5 4 3 2 1`).
2. Add the **ascending** half (`2 3 4 5`).
3. Add the **leading spaces** so it centers.

Each row needs **three** inner loops: spaces, counting down, and counting up.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get number-pyramid
cd number-pyramid
ccm test
```

Then paste all of `Main.java` into the assignment.
