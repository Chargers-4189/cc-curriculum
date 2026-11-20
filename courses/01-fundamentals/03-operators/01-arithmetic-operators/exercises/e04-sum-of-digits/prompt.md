---
title: "Sum of Digits"
type: practice
difficulty: medium
---

Read a whole number from 0 to 999 and add up its digits.

```
Enter a number between 0 and 999: 932
The sum of the digits is 14
```

`9 + 3 + 2 = 14`

**Hints:**
- `932 % 10` gives `2`, the last digit.
- `932 / 10` gives `93`, which removes the last digit.
- Do that three times.

*Adapted from Programming Exercise 2.6 in Introduction to Java Programming (Liang).*

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get sum-of-digits
cd sum-of-digits
ccm test
```
