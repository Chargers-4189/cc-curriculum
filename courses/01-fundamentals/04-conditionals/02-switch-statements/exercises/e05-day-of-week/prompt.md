---
title: "Day of the Week"
type: homework
difficulty: hard
---

**Zeller's congruence** is an algorithm developed by Christian Zeller to calculate the day of the week:

```
h = (q + 26(m + 1) / 10 + k + k / 4 + j / 4 + 5j) % 7
```

- `h` is the day of the week: 0 is Saturday, 1 is Sunday, 2 is Monday, ... 6 is Friday
- `q` is the day of the month
- `m` is the month: 3 is March ... 12 is December. **January and February count as months 13 and 14 of the previous year.**
- `j` is the century: `year / 100`
- `k` is the year of the century: `year % 100`

All of the divisions are **integer division**.

Write a program that asks for a year, month, and day of the month, and prints the name of the day of the week:

```
Enter year: (e.g., 2012): 2015
Enter month: 1-12: 1
Enter the day of the month: 1-31: 25
Day of the week is Sunday
```

**Requirements:**
- The prompts are in your starter code. Read the year, month, and day in that order.
- Print the result exactly as `Day of the week is <Day>`.
- Use a `switch` statement to turn `h` into the day's name.

**Hints:**
- Handle January and February first: if the month is 1 or 2, add 12 to the month and subtract 1 from the year. Then calculate `j` and `k`.
- `26(m + 1)` means `26 * (m + 1)`. Java needs the `*`.
- Check it with today's date.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get day-of-week
cd day-of-week
ccm test
```

Then paste all of `Main.java` into the assignment.
