---
title: "Grade Report"
type: practice
difficulty: hard
---

Put it all together. Read how many students there are and their scores, then print a report with each score's letter grade, the class average, and the highest score.

```
How many students? 3
Enter the scores: 95 82 67
Student 1: 95 (A)
Student 2: 82 (B)
Student 3: 67 (D)
Average: 81.33333333333333
Highest: 95
```

Grades: 90 and up is `A`, 80+ is `B`, 70+ is `C`, 60+ is `D`, below 60 is `F`.

Write a method for the letter grade:

```java
public static char letterGrade(int score)
```

**Hints:**
- Students are numbered starting at **1**, but array indexes start at **0**.
- `char`s use single quotes: `return 'A';`

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get grade-report
cd grade-report
ccm test
```
