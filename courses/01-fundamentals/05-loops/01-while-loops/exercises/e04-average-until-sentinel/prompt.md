---
title: "Average Until -1"
type: practice
difficulty: medium
---

Read scores until the user enters `-1` (the sentinel). Then print how many scores were entered and their average.

```
Enter a score (-1 to stop): 90
Enter a score (-1 to stop): 80
Enter a score (-1 to stop): 75
Enter a score (-1 to stop): -1
Count: 3
Average: 81.66666666666667
```

If the very first score is `-1`, print `No scores entered` instead.

**Hints:**
- Read once **before** the loop, and again at the **bottom** of the loop.
- Watch out for integer division when you calculate the average.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get average-until-sentinel
cd average-until-sentinel
ccm test
```
