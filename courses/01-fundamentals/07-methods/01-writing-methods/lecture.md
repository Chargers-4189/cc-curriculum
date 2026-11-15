> **Objectives**
> - Explain why methods exist
> - Read and write a method header: modifiers, return type, name, parameters
> - Choose between `void` and value-returning methods
> - Explain pass-by-value and why `swap` doesn't work
> - Know where a variable can be used (scope)
>
> **Prerequisites**
> - [For Loops](../../05-loops/02-for-loops/lecture.md)
> - [If Statements](../../04-conditionals/01-if-statements/lecture.md)

## Follow Along

Write `Methods.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get methods-demo` and open `Methods.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one. Your method **calls** go in `main` under the matching section comment, and the methods themselves go below `main` (inside the class).

## Why Methods?

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

## Anatomy of a Method

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

## void vs Value-Returning

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

Which is better? Usually the one that **returns**. A method that returns the grade can be printed, stored, compared, or fed into something else. A method that prints the grade can only print it.

> [!WARNING]
> **Try it:** add `double grade = printGrade(20.3);` to `main`. It won't compile, because `printGrade` doesn't give anything back. Read the error, then comment that line out.

If a method promises to return an `int`, **every path** out of it must return an `int`. The compiler checks this.

A method that answers a yes/no question returns a `boolean` and is named like a question: `isPrime`, `isValid`, `isLeapYear`. Then `if (isLeapYear(year))` is easy to read.

## Pass-by-Value

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

Java **passes a copy of the value**. `n1` and `n2` are new variables that start with the same values as `num1` and `num2`. Swapping the copies does nothing to the originals, and when the method ends, the copies are gone.

```
  main               swap
num1 [ 1 ]  --->  n1 [ 1 ]
num2 [ 2 ]  --->  n2 [ 2 ]
```

Values are copied in when the method is called, and nothing is copied back. To get a value out of a method, **return** it.

## Scope

A variable exists from where it's declared to the **closing brace** of the block it's in. Outside that block, it doesn't exist.

```java
for (int n = 0; n < 3; n++) {
    int doubled = n * 2;
}
// System.out.println(n);       // won't compile: n only existed in the loop
// System.out.println(doubled); // same
```

> [!WARNING]
> **Try it:** under `// --- Scope ---`, type the loop (print `doubled` inside it), then add the two prints after it **without** the `//`. They won't compile. Read the errors, then comment them back out.

- A variable declared in a for loop's header can't be used after the loop. If you need it later, declare it before the loop.
- Variables declared inside a method only exist in that method. Two different methods can each have a variable named `count` with no conflict.
- **Parameters are just local variables** that got their starting value from the caller. That's why `swap` didn't work.

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

## Review Quiz

[Methods Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Max of Three

[Max of Three](exercises/e02-max-of-three/prompt.md)

### 2. Prime Checker

[Prime Checker](exercises/e03-prime-checker/prompt.md)

### 3. Sum the Digits

[Sum the Digits](exercises/e04-digit-sum-method/prompt.md)

## Homework

### Credit Card Validator

[Credit Card Validator](exercises/e05-credit-card-validator/prompt.md)
