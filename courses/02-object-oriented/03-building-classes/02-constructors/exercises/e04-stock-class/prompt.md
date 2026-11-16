---
title: "Stock Class"
type: homework
difficulty: medium
---

`main` is already written. Write the `Stock` class it uses.

A `Stock` **knows**:

- `symbol` (a `String`, like `ORCL`)
- `name` (a `String`, like `Oracle Corporation`)
- `previousClosingPrice` (a `double`: the price at the end of yesterday)
- `currentPrice` (a `double`: the price right now)

A `Stock` has **two constructors**:

- One that takes the symbol and name
- One that takes the symbol, name **and** previous closing price

A `Stock` **does** one thing: `getChangePercent()` gives back how much the price changed, as a percent:

```
(currentPrice - previousClosingPrice) / previousClosingPrice * 100
```

When it works, the program prints:

```
Oracle Corporation (ORCL): -0.43%
Apple Inc. (AAPL): 5.00%
```

**Hints:**
- Look at which constructor each line of `main` calls, and how many arguments it passes.
- If you name your parameters the same as your instance variables, you need `this`.

*Adapted from Programming Exercise 9.2 in Introduction to Java Programming (Liang).*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get stock-class
cd stock-class
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
