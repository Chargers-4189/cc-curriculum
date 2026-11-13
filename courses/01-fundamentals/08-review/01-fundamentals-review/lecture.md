---
title: "Review"
prerequisites: [writing-methods]
---

# Review

> **Objectives**
> - Review everything in Fundamentals: variables, operators, conditionals, loops, arrays, and methods
> - Recognize the most common traps in each topic
> - Combine the topics in one program
>
> **Prerequisites:** Every lesson in this course! This is where it all comes together.

## 1. Variables and Types

```java
String firstName;        // declaration - the box exists, nothing in it
firstName = "bob";       // initialization - now something is in it
int myNum = 20;          // both at once, which is what you'll normally do

double ratio = 0.8;
char grade = 'A';        // single quotes = char, double quotes = String
boolean ready = true;

int ratioInt = (int) ratio; // 0 - casting cuts off the decimal
```

The type is a promise about what can go in the box, and Java holds you to it.

## 2. Arithmetic and the Operator Traps

```java
System.out.println(17 / 5);    // 3   int / int stays int
System.out.println(17.0 / 5);  // 3.4 one double makes it all decimal
System.out.println(17 % 5);    // 2   remainder

System.out.println(Integer.MAX_VALUE + 1); // -2147483648 - overflow wraps around silently

int k = 5;
int result = k++ + ++k;        // 5 + 7
System.out.println(result + " " + k); // 12 7

System.out.println(1 + 2 + "3");  // 33
System.out.println("1" + 2 + 3);  // 123
```

## 3. Booleans and Conditions

```java
int score = 87;
System.out.println(score >= 90 && score < 100); // false
System.out.println(score < 60 || score > 80);   // true
System.out.println(!(score == 87));              // false

// else-if ladder: the FIRST true branch wins
if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else if (score >= 70) {
    System.out.println("C");
} else {
    System.out.println("F");
}
```

Traps to remember:

- `==` on Strings: use `.equals()`
- A stray semicolon after `if (...)` ends the if statement right there
- No braces means only the **next line** belongs to the if
- A switch without `break` falls through into the next case

## 4. Loops

Every loop needs a condition that's true to start with, and something in the body that eventually makes it false.

```java
int i = 1, sum = 0;
while (i < 10) {      // condition
    sum += i;         // body
    i++;              // the thing that makes it stop
}

sum = 0;
for (int n = 1; n < 10; n++) {  // the same loop, in one line
    sum += n;
}
```

- **for** when you know how many times, **while** when you don't
- Nested loops: the outer picks the row, the inner fills the row
- `break` leaves the loop, `continue` skips to the next pass
- Off by one: `n <= 10` runs ten times, `n < 10` runs nine

## 5. Arrays

```java
int[] scores = {90, 85, 72, 100, 64};
for (int j = 0; j < scores.length; j++) {
    System.out.println(scores[j]);
}
```

Indexes start at 0, and the last one is `length - 1`.

## 6. Methods

```java
public static int max(int num1, int num2) {
    if (num1 > num2) {
        return num1;
    }
    return num2;
}
```

- The header is a contract: give me these things, I give you back that type
- `void` methods do something; value-returning methods produce something
- Java is **pass-by-value**: methods get copies, so `swap` can't swap the caller's variables
- A variable lives until the closing brace of its block

## 7. All of It in One Program

```java
public static boolean isPrime(int number) {
    if (number < 2) {
        return false;
    }
    for (int divisor = 2; divisor <= number / 2; divisor++) {
        if (number % divisor == 0) {
            return false; // one divisor is enough - leave immediately
        }
    }
    return true;
}

public static int countPrimesBelow(int limit) {
    int count = 0;
    for (int n = 2; n < limit; n++) {
        if (isPrime(n)) {
            count++;
        }
    }
    return count;
}
```

`countPrimesBelow` uses a method that uses a loop that uses a condition that uses the `%` operator. That's the whole course so far, stacked. Notice how `main` can stay short and read like a summary: `System.out.println(countPrimesBelow(50));`

## Practice

Pick two:

1. **Fix the traps.** Each of these compiles or runs but is wrong. Say why, then fix it.
   - `double avg = (90 + 85 + 80) / 3;` (it prints 85.0, is that luck?)
   - `if (name == "steve") { ... }`
   - `if (score > 60);  System.out.println("pass");`
   - `if (grade >= 70) letter = 'C'; else if (grade >= 90) letter = 'A';`
2. **Temperature table.** Write `printTable(int startF, int endF, int step)` that prints a Fahrenheit to Celsius table. `C = (F - 32) * 5 / 9`, and that formula has an integer division bug in it. Find it.
3. **Digit workout.** Write `countDigits(4520)` → 4, `sumOfDigits(4520)` → 11, `reverse(456)` → 654, and `isPalindrome(121)` → true. Write `reverse` first, then `isPalindrome` in one line using it.
4. **Pyramid, again.** The Number Pyramid homework, but as a method `printPyramid(int lines)` called from `main` for 3, 5, and 7 lines.

## Exercises

- [Review Problems](exercises/e01-review-problems/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get review-problems         # Review Problems
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get fundamentals-review`.

Tip: keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.
