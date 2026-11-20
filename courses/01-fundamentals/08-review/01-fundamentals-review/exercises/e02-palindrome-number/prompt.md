---
title: "Palindrome Number"
type: practice
difficulty: medium
---

A **palindrome** reads the same forwards and backwards, like `121` or `4554`. Write two methods:

```java
public static int reverse(int number)        // reverse(456) -> 654
public static boolean isPalindrome(int number) // isPalindrome(121) -> true
```

Write `reverse` first. Then `isPalindrome` is **one line** that uses it.

```
Enter a number: 121
121 reversed is 121
121 is a palindrome
```

```
Enter a number: 456
456 reversed is 654
456 is not a palindrome
```

**Hint:** to build the reversed number, take the last digit off `number` and add it to the end of `reversed`: `reversed = reversed * 10 + number % 10`.

*Adapted from Programming Exercise 6.3 in Introduction to Java Programming (Liang).*

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get palindrome-number
cd palindrome-number
ccm test
```
