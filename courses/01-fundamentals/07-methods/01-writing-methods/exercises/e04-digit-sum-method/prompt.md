---
title: "Sum the Digits"
type: practice
difficulty: medium
---

Write a method that adds up all the digits in a number, no matter how many digits it has:

```java
public static int sumDigits(long n)
```

`sumDigits(234)` returns `2 + 3 + 4 = 9`.

```
Enter a number: 4520
Sum of digits: 11
```

**Hints:**
- `n % 10` is the last digit and `n / 10` removes it.
- Loop while `n > 0`. Since `n` is a parameter (a copy!), changing it inside the method doesn't change anything in `main`.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get digit-sum-method
cd digit-sum-method
ccm test
```
