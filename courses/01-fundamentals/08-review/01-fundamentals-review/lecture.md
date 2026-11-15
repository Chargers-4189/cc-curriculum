> **Objectives**
> - Review everything in Fundamentals: variables, operators, conditionals, loops, arrays, and methods
> - Recognize the most common traps in each topic
> - Combine the topics in one program
>
> **Prerequisites:** every lesson in this course

## 1. Variables and Types

```java
String firstName;        // declaration
firstName = "bob";       // initialization
int myNum = 20;          // both at once

double ratio = 0.8;
char grade = 'A';        // single quotes = char, double quotes = String
boolean ready = true;

int ratioInt = (int) ratio; // 0 - casting cuts off the decimal
```

## 2. Arithmetic and the Operator Traps

```java
System.out.println(17 / 5);    // 3   int / int stays int
System.out.println(17.0 / 5);  // 3.4 one double makes it all decimal
System.out.println(17 % 5);    // 2   remainder

System.out.println(Integer.MAX_VALUE + 1); // -2147483648 - overflow

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

Every loop needs a condition and something in the body that eventually makes it false.

```java
int i = 1, sum = 0;
while (i < 10) {      // condition
    sum += i;         // body
    i++;              // makes it stop
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
            return false; // one divisor is enough
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

`countPrimesBelow` uses a method, a loop, a condition, and `%`. `main` stays short: `System.out.println(countPrimesBelow(50));`

## Review Quiz

[Fundamentals Review Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes.

### 1. Temperature Table

[Temperature Table](exercises/e01-temperature-table/prompt.md)

### 2. Palindrome Number

[Palindrome Number](exercises/e02-palindrome-number/prompt.md)

### 3. Grade Report

[Grade Report](exercises/e03-grade-report/prompt.md)

## Homework

### Days From Today

[Days From Today](exercises/e04-days-from-today/prompt.md)

### Quadratic Roots

[Quadratic Roots](exercises/e05-quadratic-roots/prompt.md)
