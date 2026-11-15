> **Objectives**
> - Use `if`, `else if`, and `else` to choose which code runs
> - Order an `else if` ladder correctly
> - Nest if statements, and simplify them with logical operators
> - Spot the missing-braces and stray-semicolon traps
> - Guard against errors like dividing by zero
>
> **Prerequisites:** [Relational and Logical Operators](../../03-operators/02-relational-and-logical-operators/lecture.md)

## Follow Along

Write `Conditional.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get conditional-demo` and open `Conditional.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one.

## Conditionals

Recall the different errors that can arise in our programs, such as dividing by zero. If we wanted to avoid this, how can we implement this into our program?

Java provides us with **conditionals**. These give us **decision points** in the program to decide what to do.

- Conditionals use **boolean** expressions
- If the boolean expression in the parentheses is `true`, the code inside is run
  - Otherwise, the code is **skipped**
- Logical operators can be used to check multiple conditions

![If statement flowchart](assets/slide-if-flowchart.png)

## The if Statement

```java
if (condition) {
    System.out.println("Only runs if condition is true");
}
System.out.println("Runs regardless");
```

If statements allow you to program different paths of computing. This decision making is done through the condition, which must be a **boolean**.

```java
int r = -2;
if (r <= 0) {
    System.out.println("Retype radius above 0");
}
```

## if / else

`else` runs **only if** the `if` condition was `false`. Exactly one of the two blocks will run.

```java
double r = 1.0;
if (r <= 0) {
    System.out.println("Retype radius above 0");
} else {
    System.out.println(r * r * 3.14); // area of the circle
}
```

## else if

When there are more than two paths, chain them with `else if`:

```java
int age = 22;
if (age >= 16) {
    System.out.println("You can drive");
} else if (age >= 21) {
    System.out.println("You can rent a car");
} else {
    System.out.println("You cannot drive");
}
```

- `if` runs if its condition is `true`
- `else if` runs only if every condition before it was `false` **and** its own condition is `true`
- `else` runs if **none** of the conditions were `true`

Run this with `age = 22`. It prints "You can drive", never "You can rent a car". The **first true branch wins** and the rest are skipped. Since every 22-year-old is also `>= 16`, the `age >= 21` branch can never be reached.

**Order matters.** Put the most specific condition first:

```java
if (age >= 21) {
    System.out.println("You can rent a car");
} else if (age >= 16) {
    System.out.println("You can drive");
} else {
    System.out.println("You cannot drive");
}
```

## Nested if Statements

You can put an if statement inside another:

```java
int age = 22;
boolean hasID = true;
if (age >= 18) {
    if (hasID) {
        System.out.println("Entry allowed.");
    } else {
        System.out.println("Old enough, but ID required.");
    }
} else {
    System.out.println("Not old enough");
}
```

The same logic can often be flattened with `&&`:

```java
if (age >= 18 && hasID) {
    System.out.println("Entry allowed.");
} else if (age >= 18 && !hasID) {
    System.out.println("Old enough, but ID required.");
} else {
    System.out.println("Not old enough");
}
```

Use whichever is easier to read.

## Guarding Against Errors

Remember short-circuiting? `&&` skips the right side when the left is `false`. We can use that to prevent a crash:

```java
int dividend = 10;
int divisor = 0;
if (divisor != 0 && dividend / divisor == 2) {
    System.out.println("Runs");
} else {
    System.out.println("Error: divide by zero.");
}
```

And for decimals, compare with a threshold instead of `==`:

```java
double total = 0.1 + 0.2;
if (Math.abs(total - 0.3) < 1e-9) {
    System.out.println("Total is close enough.");
}
```

> [!WARNING]
> **Try it:** swap the two sides of the `&&` (put the division first) and run it. It crashes! Swap them back.

## Common Traps

**Missing braces.** Without `{ }`, only the **next line** belongs to the if:

```java
boolean loggedIn = false;
if (loggedIn)
    System.out.println("Welcome Back!");
    System.out.println("This prints even though loggedIn is false");
```

Java ignores the indentation, so always use braces.

**Stray semicolon.** A `;` right after the condition ends the if statement immediately:

```java
int n = -5;
if (n > 0); // <- this semicolon is the whole if statement
{
    System.out.println("This prints, even though n is -5");
}
```

**Using `=` instead of `==`.** `if (x = 5)` doesn't compile, because the condition must be a boolean.

> [!WARNING]
> **Try it:** type the stray semicolon trap too. Then try `if (n = 5) { }`, read the error, and **comment it out** so your file compiles again.

## Further

- **Ternary operator:** a short if/else that produces a value.

  ```java
  String label = (score % 2 == 0) ? "even" : "odd";
  // condition ? value if true : value if false
  ```

- **Dangling else:** without braces, an `else` belongs to the **closest** `if`, not the one it's lined up with. Another reason to always use braces.

## Review Quiz

[If Statements Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Positive, Negative, or Zero

[Positive, Negative, or Zero](exercises/e02-positive-or-negative/prompt.md)

### 2. Letter Grade

[Letter Grade](exercises/e03-letter-grade/prompt.md)

### 3. Safe Division

[Safe Division](exercises/e04-safe-division/prompt.md)

## Homework

Each homework has its own assignment page after the lesson.

### Subtraction Quiz

[Subtraction Quiz](exercises/e05-subtraction-quiz/prompt.md)
