---
title: "Methods"
prerequisites: [for-loops]
---

# Methods

## Objectives

- Explain why methods exist
- Read and write a method header: modifiers, return type, name, parameters
- Choose between `void` and value-returning methods
- Explain pass-by-value and why `swap` doesn't work
- Know where a variable can be used (scope)

## Prerequisites

- [For Loops](../../05-loops/02-for-loops/lecture.md)
- [If Statements](../../04-conditionals/01-if-statements/lecture.md)

## Content

### Why Methods?

Here's code that sums two ranges of numbers:

```java
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}
System.out.println(sum);

sum = 0;
for (int i = 20; i <= 37; i++) {
    sum += i;
}
System.out.println(sum);
```

What is actually **different** between those two blocks? Only two numbers. Everything else is copy-paste. And if the logic has a bug, you now have two bugs to fix.

Instead, write the loop **once** in a **method**, give the two numbers names, and **call** it as many times as you want:

```java
public static int sumOfRange(int min, int max) {
    int sum = 0;
    for (int i = min; i <= max; i++) {
        sum += i;
    }
    return sum;
}
```

```java
System.out.println(sumOfRange(1, 10));   // 55
System.out.println(sumOfRange(20, 37));  // 513
System.out.println(sumOfRange(55, 101)); // 3666
```

You've been calling methods since day one: `System.out.println`, `Math.random`, `Math.abs`. Now you get to write your own.

### Anatomy of a Method

```
public static int max(int num1, int num2)
------------- --- --- -------------------
  modifiers    |   |      parameters
               |  name
          return type
```

- **Modifiers:** `public static` for now. We'll learn what they mean in Object Oriented.
- **Return type:** the type of value the method gives back (`int`, `double`, `boolean`...), or `void` if it gives nothing back
- **Name:** a verb, in camelCase
- **Parameters:** the inputs, each with its own type

Four questions to ask about any method:

- What's it called? → `max`
- What does it need? → two `int`s
- What does it give back? → one `int`
- How does it do it? → the body (and the caller doesn't need to care)

```java
public static int max(int num1, int num2) {
    if (num1 > num2) {
        return num1;
    } else {
        return num2;
    }
}
```

**Vocabulary:**

- **Parameters** are the names in the definition (`num1`, `num2`)
- **Arguments** are the actual values you pass in: in `max(5, 2)`, the arguments are `5` and `2`

Calling a method **jumps** to it and runs its body. `return` **ends the method immediately** and jumps back with the value in hand.

### void vs Value-Returning

```java
public static void printGrade(double grade) {
    System.out.println(grade);
}

public static double getGrade(double grade) {
    return grade;
}
```

- A **void** method **does** something. You call it on its own line: `printGrade(90.2);`
- A **value-returning** method **produces** something. You use it anywhere a value fits: `System.out.println(getGrade(99.3));`

Which is better? Usually the one that **returns**. A method that returns the grade can be printed, stored, compared, or fed into something else. A method that prints the grade can only ever print it.

If a method promises to return an `int`, **every path** out of it must return an `int`. The compiler checks this.

A method that answers a yes/no question returns a `boolean` and is named like a question: `isPrime`, `isValid`, `isLeapYear`. Then `if (isLeapYear(year))` reads like English.

### Pass-by-Value

Predict what this prints:

```java
public static void increment(int n) {
    n++;
    System.out.println("n inside the method is " + n);
}
```

```java
int x = 1;
System.out.println("Before: " + x);
increment(x);
System.out.println("After: " + x);
```

```
Before: 1
n inside the method is 2
After: 1
```

`x` didn't change! Same with swap:

```java
public static void swap(int n1, int n2) {
    int temp = n1;
    n1 = n2;
    n2 = temp;
    System.out.println("  inside swap: n1 = " + n1 + ", n2 = " + n2);
}
```

```java
int num1 = 1;
int num2 = 2;
swap(num1, num2);
System.out.println("After: " + num1 + " " + num2); // After: 1 2
```

Java **passes a copy of the value**. `n1` and `n2` are brand new variables that happen to start with the same values as `num1` and `num2`. Swapping the copies does nothing to the originals, and when the method ends, the copies are gone.

```
  main               swap
num1 [ 1 ]  --->  n1 [ 1 ]
num2 [ 2 ]  --->  n2 [ 2 ]
```

The arrow only goes one way, and only at the moment of the call. Methods communicate by **arguments in, return value out**.

### Scope

A variable exists from where it's declared to the **closing brace** of the block it's in. Outside that block, it doesn't exist.

```java
for (int n = 0; n < 3; n++) {
    int doubled = n * 2;
}
// System.out.println(n);       // won't compile: n only existed in the loop
// System.out.println(doubled); // same
```

- A variable declared in a for loop's header can't be used after the loop. If you need it later, declare it before the loop.
- Variables declared inside a method only exist in that method. Two different methods can each have a variable named `count` with no conflict.
- **Parameters are just local variables** that got their starting value from the caller. That's exactly why `swap` couldn't work.

## Further

**Overloading.** Several methods can share a name if their **parameter lists** are different:

```java
public static int max(int num1, int num2) { ... }
public static double max(double num1, double num2) { ... }
public static double max(double num1, double num2, double num3) {
    return max(max(num1, num2), num3); // methods calling methods
}
```

Java picks which one to run based on the arguments. You've been using this already: `System.out.println` accepts an `int`, a `double`, a `String`... Changing only the return type isn't enough.

**Stepwise refinement.** When a program is too big to picture, break it into methods you **can** write, and start each one as a **stub** that returns a dummy value:

```java
public static boolean isLeapYear(int year) {
    return true; // TODO - dummy for now
}
```

Write `main`, stub everything it calls, and run it. Then fill in one stub at a time, running as you go. You always have a working program, and when something breaks, you know it's in the method you just touched. This is how the Credit Card Validator homework is meant to be done.

## Review

- What are the four parts of a method header?
- What's the difference between a parameter and an argument?
- When would you use `void` instead of returning a value?
- Why doesn't `swap(num1, num2)` swap `num1` and `num2`?
- Can you use a for loop's counter variable after the loop ends?

## Exercises

- [Methods (Follow Along)](exercises/e01-methods-demo/prompt.md)
- [Credit Card Validator (Homework)](exercises/e02-credit-card-validator/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get methods-demo            # Methods (Follow Along)
ccm get credit-card-validator   # Credit Card Validator (Homework)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get writing-methods`.

Tip: keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.

To check homework, run `ccm test` from inside its folder:

```bash
cd credit-card-validator
ccm test
```
