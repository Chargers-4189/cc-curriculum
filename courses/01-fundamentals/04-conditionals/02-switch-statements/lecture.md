> **Objectives**
> - Write a `switch` statement with `case`, `break`, and `default`
> - Explain fall-through and why `break` is needed
> - Decide when a `switch` reads better than an `else if` ladder
>
> **Prerequisites:** [If Statements](../01-if-statements/lecture.md)

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

## Review

- What does `default` do in a switch?
- What happens if you leave out a `break`?
- Could you use a switch to check if `score >= 90`? Why or why not?

## Exercises

- [Day of the Week (Homework)](exercises/e01-day-of-week/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get day-of-week             # Day of the Week (Homework)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get switch-statements`.

> [!TIP]
> Keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.

To check homework, run `ccm test` from inside its folder:

```bash
cd day-of-week
ccm test
```
