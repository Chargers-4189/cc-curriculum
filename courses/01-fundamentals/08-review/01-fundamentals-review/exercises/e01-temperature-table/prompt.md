---
title: "Temperature Table"
type: practice
difficulty: medium
---

Write a method that prints a Fahrenheit to Celsius table:

```java
public static void printTable(int startF, int endF, int step)
```

Each row is the Fahrenheit temperature, a space, then the Celsius temperature as a whole number, using `C = (F - 32) * 5 / 9`.

```
Enter start, end, and step: 32 212 45
32 0
77 25
122 50
167 75
212 100
```

The starter's formula has the classic **integer division** bug in it. Run the tests and look at which rows are wrong, then fix the order of operations so it matches the table above.

**Hint:** `5 / 9` is `0`. What happens if you multiply by 5 **before** dividing by 9?

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get temperature-table
cd temperature-table
ccm test
```
