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

**Hint:** `%` gives 0 to 6. Subtract 1 from the day before using `%`, then add 1 back.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get days-from-today
cd days-from-today
ccm test
```

Then paste all of `Main.java` into the assignment.
