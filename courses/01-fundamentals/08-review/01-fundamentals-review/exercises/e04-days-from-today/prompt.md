---
title: "Days From Today"
type: homework
difficulty: medium
---

Number the days of the week from 1 to 7, where 1 is Monday and 7 is Sunday. Ask for today's day and a number of days, then print what day it will be.

```
Enter today's day (1 = Monday ... 7 = Sunday): 5
Enter the number of days: 50
In 50 days it will be day 6
```

So if today is Friday (5), in 50 days it will be Saturday (6). Use only arithmetic operators (`+ - * / %`), no loops or if statements.

**Hint:** `%` wraps around, but it gives 0 to 6, not 1 to 7. Shift the day down by 1 before you use `%`, then shift it back up.

*Adapted from Programming Exercise 3.5 in Introduction to Java Programming (Liang).*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get days-from-today
cd days-from-today
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
