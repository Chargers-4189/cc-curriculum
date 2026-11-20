> **Objectives**
> - Write a `switch` statement with `case`, `break`, and `default`
> - Explain fall-through and why `break` is needed
> - Decide when a `switch` reads better than an `else if` ladder
>
> **Prerequisites:** [If Statements](../01-if-statements/lecture.md)

*Parts of this lesson are adapted from Introduction to Java Programming (Liang), 3.9 and 3.13.*

## Follow Along

Write `Switch.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get switch-demo` and open `Switch.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one.

## The Problem

Imagine a tax form application that asks for the user's filing status:

- 0: Single
- 1: Married / Widow
- 2: Married filing separately
- 3: Head of household

With if statements, that's a long ladder that checks the same variable over and over:

```java
int status = 0;
if (status == 0) {
    System.out.println("You're filing single");
} else if (status == 1) {
    System.out.println("You're filing as married");
} else if (status == 2) {
    System.out.println("You're filing as married separately");
} else if (status == 3) {
    System.out.println("You're filing as head of household");
}
```

## The switch Statement

A `switch` does the same job when you're comparing **one value** against a list of **exact matches**:

```java
switch (status) {
    case 0:
        System.out.println("You're filing single");
        break;
    case 1:
        System.out.println("You're filing as married");
        break;
    case 2:
        System.out.println("You're filing as married separately");
        break;
    case 3:
        System.out.println("You're filing as head of household");
        break;
    default:
        System.out.println("Error, please retype status");
}
```

- `switch (status)` - the value being checked
- `case 0:` - runs when `status` equals 0
- `break;` - jumps out of the switch
- `default:` - runs when **no** case matched, like a final `else`

A switch works with `int`, `char`, and `String` values (among others), but not `double` or `boolean`.

## Fall-Through

The `break`s prevent **fall-through**. Without a `break`, Java keeps running every case below the one that matched, including `default`:

```java
int status = 1;
switch (status) {
    case 0:
        System.out.println("Single");
    case 1:
        System.out.println("Married");
    case 2:
        System.out.println("Married separately");
    default:
        System.out.println("Error");
}
```

This prints `Married`, `Married separately`, and `Error`. Forgetting a `break` is the most common switch bug.

Sometimes fall-through is useful, when several cases share the same code:

```java
switch (day) {
    case 1:
    case 7:
        System.out.println("Weekend");
        break;
    default:
        System.out.println("Weekday");
}
```

## switch or if?

- Use a **switch** when you're checking one variable for **equality** against a list of fixed values (menus, days, status codes).
- Use **if** statements for **ranges** and complex conditions (`score >= 90`, `age >= 18 && hasID`). A switch can't do those.

## Further

Newer versions of Java (14+) have a shorter **arrow** form that never falls through, so it doesn't need `break`:

```java
switch (status) {
    case 0 -> System.out.println("You're filing single");
    case 1 -> System.out.println("You're filing as married");
    default -> System.out.println("Error, please retype status");
}
```

You'll see both forms in other people's code.

## Review Quiz

[Switch Statements Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Month Name

[Month Name](exercises/e02-month-name/prompt.md)

### 2. Calculator

[Calculator](exercises/e03-calculator/prompt.md)

### 3. Weekday or Weekend

[Weekday or Weekend](exercises/e04-weekday-or-weekend/prompt.md)

## Homework

### Day of the Week

[Day of the Week](exercises/e05-day-of-week/prompt.md)

## Readings

### Further

- Introduction to Java Programming (Liang), 3.13: switch Statements
