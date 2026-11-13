---
title: "Leap Years (Homework)"
---

# Leap Years (Homework)

## Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get leap-years
cd leap-years
ccm test        # check your work
```

## Task

Write a program, `LeapYears.java`, that displays all the leap years, **ten per line**, from 101 to 2100, separated by exactly one space. Also display the number of leap years in this period.

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
- Print the years in order, 10 per line.
- End with a line that includes the total number of leap years.

**Hints:**
- Use a counter to know when you've printed 10 on a line, then `System.out.println()` and reset it.
- `%` is your friend for "divisible by".

Run `ccm test` to check your work.
