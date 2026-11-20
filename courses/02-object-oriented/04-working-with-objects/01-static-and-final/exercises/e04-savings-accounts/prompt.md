---
title: "Savings Accounts"
type: homework
difficulty: medium
---

A bank gives every account the **same** interest rate, and every account gets its own ID number. `main` is already written. Write the `Account` class it uses.

Shared by every account (**static**):

- `interestRate`, a `double`: the yearly rate as a percent (`4.5` means 4.5%). It starts at `0`
- `nextId`, an `int` that starts at `1001`
- `setInterestRate(double rate)` and `getInterestRate()`

Each account (**not** static, and **private**):

- `id`, an `int` that's **final**. The first account made gets 1001, the next gets 1002, and so on
- `balance`, a `double`
- A constructor that takes the starting balance
- `getId()` and `getBalance()`
- `deposit(double amount)`, which ignores amounts that aren't more than 0
- `getMonthlyInterest()`, which gives back `balance * interestRate / 100 / 12`

When it works, the program prints:

```
Account #1001: $20000.0
Account #1002: $1200.0
Quinn earns $75.00 a month
Caleb earns $4.50 a month
The rate is now 6.0%
Quinn earns $100.00 a month
Caleb earns $7.50 a month
Caleb has $1500.0
```

**Hints:**
- Notice that `main` changes the rate **once**, and both accounts earn more. That's what a static variable does.
- The constructor uses `nextId` to set `id`, then moves `nextId` up by one.

*Adapted from Programming Exercise 9.7 in Introduction to Java Programming (Liang).*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get savings-accounts
cd savings-accounts
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
