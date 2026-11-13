---
title: "Arithmetic Operators"
prerequisites: [variables-and-data-types]
lms_source: https://chargingcourses.com/lms/courses/1-fundamentals/learn/3-2
---

# Arithmetic Operators

> **Objectives**
> - Use Java's arithmetic operators: `+ - * / %`
> - Predict the difference between integer and floating-point division
> - Recognize integer overflow
> - Use increment, decrement, and compound assignment operators
> - Join text and values with String concatenation
>
> **Prerequisites:** [Variables and Data Types](../../02-java-basics/03-variables-and-data-types/lecture.md)

## Operators

Java has a few families of operators. We'll start with arithmetic, then cover the rest in the next lesson.

- **Arithmetic operators** are used for performing mathematical calculations
- **Relational operators** are used to compare values, returning a true or false result
- **Logical operators** are used to combine boolean values to make complex decisions
- **Order of operations** is similar to PEMDAS, and parentheses override the default order

## Basic Mathematical Operators

Java provides basic mathematical operators that can be used on variables and values.

| Operator | Name | Example (`a = 17, b = 5`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `22` |
| `-` | Subtraction | `a - b` | `12` |
| `*` | Multiplication | `a * b` | `85` |
| `/` | Division | `a / b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `2` |

```java
int a = 17, b = 5;
System.out.println(a + b); // 22
System.out.println(a - b); // 12
System.out.println(a * b); // 85
System.out.println(a / b); // 3
System.out.println(a % b); // 2
```

You'll use these in real calculations all the time:

```java
totalProfit = totalRevenue - totalExpense;
leftOver = totalCookies % totalCustomers;
```

### Modulus

`%` gives you the **remainder** after division. `17 / 5` is 3 with 2 left over, so `17 % 5` is `2`.

Modulus is more useful than it looks:

- `n % 2 == 0` checks if a number is **even**
- `n % 10` gives you the **last digit** of a number
- It "wraps around", which is perfect for things like days of the week

## Integer Division vs Floating-point Division

When dividing two values, their data types change what division will be done.

- If **both** values are integers, Java does **integer division**: the decimal is cut off.
- If **either** value is a `double`, the whole expression is calculated as **floating-point** (decimal) division.

```java
System.out.println(17 / 5);     // 3   - int / int stays int
System.out.println(17.0 / 5);   // 3.4 - one double makes it all decimal
System.out.println(3 / 4);      // 0   - 0.75, with the decimal cut off
System.out.println(3 / 4.0);    // 0.75
```

This is one of the most common bugs in Java. If you want a decimal answer, make sure one side is a `double`.

You also can't divide an integer by zero. `10 / 0` crashes the program with an `ArithmeticException`.

## Integer Overflow

An `int` can only hold up to `2147483647` (`Integer.MAX_VALUE`). Go past it and the value **rolls over** to the most negative number, with no warning:

```java
int max = Integer.MAX_VALUE;
System.out.println(max + 1); // -2147483648
```

## Incrementing and Decrementing

Adding or subtracting 1 is so common that Java has shortcuts:

- `j++` is equivalent to `j = j + 1`
- `j--` is equivalent to `j = j - 1`

Where you put the `++` matters when it's used inside an expression:

- `j++` (post-increment) **uses** `j` first, **then** adds 1
- `++j` (pre-increment) **adds** 1 first, **then** uses `j`

```java
int j = 5;
System.out.println(j++); // 5 - prints, then j becomes 6
System.out.println(++j); // 7 - j becomes 7, then prints

int l = 5;
int result = l++ + ++l;  // 5 + 7
System.out.println(result); // 12
System.out.println(l);      // 7
```

Tip: use `++` on its own line and you never have to think about this.

## Compound Assignment Operators

These do the math and the assignment in one step:

| Operator | Same as |
|---|---|
| `c += 5` | `c = c + 5` |
| `c -= 5` | `c = c - 5` |
| `c *= 5` | `c = c * 5` |
| `c /= 5` | `c = c / 5` |
| `c %= 5` | `c = c % 5` |

## String Concatenation

The `+` operator also **joins** text together. Java reads left to right, and once it hits a String, everything after it is joined as text:

```java
System.out.println(1 + 2);       // 3   - int + int
System.out.println(1 + 2 + "3"); // 33  - 1 + 2 is 3, then "3" is joined on
System.out.println("1" + 2 + 3); // 123 - "1" + 2 is "12", then "123"
```

This is how we print labels with values: `System.out.println("Total: " + total);`

## Order of Operations

Java follows an order similar to PEMDAS: parentheses first, then `* / %`, then `+ -`, left to right.

```java
2 * 3 + 1      // same as (2 * 3) + 1, which is 7
2 * (3 + 1)    // same as 2 * 4, which is 8
```

When in doubt, use parentheses. They make your intent clear.

## Review

- What is `17 % 5`? What about `20 % 5`?
- What does `7 / 2` print? How would you get `3.5`?
- What happens when you add 1 to `Integer.MAX_VALUE`?
- If `k = 5`, what does `System.out.println(k++);` print? What is `k` afterward?
- What does `"Score: " + 4 + 5` print?

## Exercises

- [Arithmetic (Follow Along)](exercises/e01-arithmetic-demo/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get arithmetic-demo         # Arithmetic (Follow Along)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get arithmetic-operators`.

Tip: keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.
