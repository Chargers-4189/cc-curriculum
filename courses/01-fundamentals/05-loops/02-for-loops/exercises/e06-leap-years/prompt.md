---
title: "Leap Years"
type: homework
difficulty: medium
---

Print all the leap years from 101 to 2100, **ten per line**, separated by exactly one space. Then print how many there were.

```
Leap Years between 101 and 2100:
104 108 112 116 120 124 128 132 136 140
144 148 152 156 160 164 168 172 176 180
...
Total leap years is <count>
```

A year is a **leap year** if it is divisible by 4 but not by 100, **or** it is divisible by 400.

- 2024 is a leap year (divisible by 4, not by 100)
- 1900 is **not** a leap year (divisible by 100, not by 400)
- 2000 **is** a leap year (divisible by 400)

**Requirements:**
- The first line is exactly `Leap Years between 101 and 2100:`
- Print the years in order, 10 per line (the last line can have fewer).
- End with `Total leap years is ` and the count.

**Hints:**
- Use a counter to know when you've printed 10 on a line, then `System.out.println()` and reset it.
- `%` is your friend for "divisible by".

*Adapted from Programming Exercise 5.27 in Introduction to Java Programming (Liang).*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get leap-years
cd leap-years
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
