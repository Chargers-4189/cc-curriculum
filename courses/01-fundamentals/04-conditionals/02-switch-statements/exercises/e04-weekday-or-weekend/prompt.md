---
title: "Weekday or Weekend"
type: practice
difficulty: medium
---

Days are numbered 1 to 7, where 1 is Monday and 7 is Sunday. Read a day number and print `Weekday`, `Weekend`, or `Invalid day`.

```
Enter a day (1-7): 6
Weekend
```

Use **fall-through** so you don't repeat the same `println` five times.

**Hint:** stack cases with nothing between them:

```java
case 6:
case 7:
    ...
```

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get weekday-or-weekend
cd weekday-or-weekend
ccm test
```
