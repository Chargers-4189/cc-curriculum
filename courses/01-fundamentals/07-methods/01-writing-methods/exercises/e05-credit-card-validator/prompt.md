---
title: "Credit Card Validator"
type: homework
difficulty: hard
---

Credit card numbers follow certain patterns. A valid number:

- Has **13 to 16 digits**
- Starts with **4** (Visa), **5** (Mastercard), **37** (American Express), or **6** (Discover)
- Passes the **Luhn check**:
  1. Double every second digit from the right. If doubling gives two digits, add those two digits together (e.g. `8 * 2 = 16` → `1 + 6 = 7`).
  2. Sum those results.
  3. Sum the digits in the odd positions from the right.
  4. Add steps 2 and 3. If the total is divisible by 10, the card is valid.

Test data: `4388576018410707` is valid, `4388576018402626` is invalid.

Write a program that reads a card number as a `long` and prints whether it is valid:

```
Enter a credit card number as a long integer: 4388576018410707
4388576018410707 is valid
```

```
Enter a credit card number as a long integer: 4388576018402626
4388576018402626 is invalid
```

**Required methods.** Fill in the bodies of these headers (they're already in your starter code):

```java
/** Return true if the card number is valid */
public static boolean isValid(long number)

/** Get the result from Step 2 */
public static int sumOfDoubleEvenPlace(long number)

/** Return this number if it is a single digit, otherwise return the sum of the two digits */
public static int getDigit(int number)          // getDigit(12) -> 3, getDigit(7) -> 7

/** Return the sum of the odd-place digits in number (Step 3) */
public static int sumOfOddPlace(long number)

/** Return true if the number d is a prefix for number */
public static boolean prefixMatched(long number, int d)

/** Return the number of digits in d */
public static int getSize(long d)               // getSize(4388) -> 4

/** Return the first k digits of number. If number has fewer than k digits, return number. */
public static long getPrefix(long number, int k) // getPrefix(4388576018410707L, 2) -> 43
```

**How to approach it:** this is a lot to write at once, so build it one method at a time.

1. Every method starts as a **stub** that returns a dummy value, so your program compiles from the start.
2. Implement the easy ones first: `getDigit`, then `getSize`. Test each one by printing it from `main` (e.g. `System.out.println(getDigit(12));`), then delete the test print.
3. Then `getPrefix` and `prefixMatched`, then the two sums.
4. Only then put it together in `isValid` and `main`.

**Hints:**
- `number % 10` gives the last digit; `number / 10` removes it.
- Use `long` for the card number. It's too big for an `int`; long literals end in `L`: `4388576018410707L`.
- In Labs, `ccm test` also checks each method on its own, so you can see your progress one method at a time.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get credit-card-validator
cd credit-card-validator
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
