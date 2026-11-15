> **Objectives**
> - Use Java's arithmetic operators: `+ - * / %`
> - Predict the difference between integer and floating-point division
> - Recognize integer overflow
> - Use increment, decrement, and compound assignment operators
> - Join text and values with String concatenation
>
> **Prerequisites:** [Variables and Data Types](../../02-java-basics/03-variables-and-data-types/lecture.md)

## Follow Along

You'll write `Arithmetic.java` in this lesson. Open a terminal in **Charging Courses Labs** and run:

```bash
mkdir -p fundamentals/week2
cd fundamentals/week2
ccm get arithmetic-demo
cd arithmetic-demo
```

Then open `Arithmetic.java` from the Explorer. It has a comment for each section, like `// --- Type Casting ---`. Write each section's code under its comment and run it. If a name is already used, pick a new one.

> [!TIP]
> Keep downloads organized in folders like `fundamentals/week1` and `fundamentals/hwk`. See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized).

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

Common uses:

- `n % 2 == 0` checks if a number is **even**
- `n % 10` gives you the **last digit** of a number
- It "wraps around", like days of the week

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

If you want a decimal answer, make one side a `double`.

You also can't divide an integer by zero. `10 / 0` crashes the program with an `ArithmeticException`.

> [!WARNING]
> **Try it:** add `System.out.println(10 / 0);` and run it to see the crash. Then comment it out.

## Integer Overflow

An `int` can only hold up to `2147483647` (`Integer.MAX_VALUE`). Go past it and the value **rolls over** to the most negative number, with no warning:

```java
int max = Integer.MAX_VALUE;
System.out.println(max + 1); // -2147483648
```

## Incrementing and Decrementing

Java has shortcuts for adding or subtracting 1:

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

> [!TIP]
> Put `++` on its own line so the order doesn't matter.

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

When in doubt, use parentheses.

## Review Quiz

[Arithmetic Operators Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes.

### 1. Seconds to Minutes

[Seconds to Minutes](exercises/e02-seconds-to-minutes/prompt.md)

### 2. Fahrenheit to Celsius

[Fahrenheit to Celsius](exercises/e03-fahrenheit-to-celsius/prompt.md)

### 3. Sum of Digits

[Sum of Digits](exercises/e04-sum-of-digits/prompt.md)
