---
title: "Prime Checker"
type: practice
difficulty: medium
---

A **prime** number is a whole number greater than 1 that can only be divided evenly by 1 and itself. Write:

```java
public static boolean isPrime(int number)
```

Then use it in `main`:

```
Enter a number: 7
7 is prime
```

```
Enter a number: 8
8 is not prime
```

**Hints:**
- Anything less than 2 is not prime.
- Try every divisor from 2 up to `number / 2`. If any divides evenly, `return false` right away.
- If the loop finishes without finding one, it's prime.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get prime-checker
cd prime-checker
ccm test
```
