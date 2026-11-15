---
title: "Divisible by 5 and 6"
type: practice
difficulty: medium
---

Read a whole number and print three things about it:

```
Enter a number: 10
Divisible by 5 and 6: false
Divisible by 5 or 6: true
Divisible by 5 or 6, but not both: true
```

**Hints:**
- Make two `boolean` variables first: `byFive` and `bySix`.
- "But not both" is true when exactly **one** of them is true. You can build it from `&&`, `||`, and `!`.
- Don't forget the parentheses around each expression when you join it to the text.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get divisible-by-5-and-6
cd divisible-by-5-and-6
ccm test
```
