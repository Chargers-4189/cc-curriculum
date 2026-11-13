---
title: "Variables and Data Types"
prerequisites: [hello-world]
---

# Variables and Data Types

> **Objectives**
> - Declare and initialize variables
> - Choose the right data type: `int`, `double`, `char`, `boolean`, `String`
> - Convert between types with type casting
> - Name variables, methods, and classes using Java conventions
> - Read input from the user with `Scanner`
>
> **Prerequisites:** [Hello World](../02-hello-world/lecture.md): writing and running a program

## Variables

Variables are just **containers**! They hold values.

- Declare with a **data type**: `String`
- Give it a **name**: `firstName`
- Initialize it with a **value**: `"Steve"`

```java
String firstName;
firstName = "Steve";
```

Variables are used in nearly every program to **store and manipulate data**: calculations, storing information, controlling program flow, and more.

## Declaration & Initialization

**Declaration** specifies the data type and name. The variable exists, but holds nothing yet.

```java
dataType variableName;
int age;
```

**Initialization** assigns a value to your variable. The `=` assigns the value on the right to the variable on the left.

```java
variableName = value;
age = 16;
```

Most of the time you'll do both at once:

```java
int age = 16;
double price = 19.99;
char grade = 'A';
boolean isJavaFun = false;
```

Once a variable exists, you can **assign it a new value** any time, but its type stays the same. `age` will always hold an `int`.

## Data Types

**Primitive data types** are the simplest data types:

| Type | Represents | Example |
|---|---|---|
| `int` | Whole numbers, positive or negative | `42`, `-7` |
| `double` | Decimal numbers | `3.14`, `-0.5` |
| `char` | A single character, in single quotes | `'A'`, `'?'` |
| `boolean` | A true or false value | `true`, `false` |

**Range & precision:**

- `int` can store about -2 billion to +2 billion (exactly -2,147,483,648 to 2,147,483,647)
- `double` can store decimals at high precision

There's one more type you'll use constantly: **`String`** holds text, in double quotes, like `"Hello World"`. It's not a primitive (we'll learn why in the Object Oriented course), but you can use it just like the others.

**Note:** Consider size and memory when choosing data types. `int` is more efficient than `double` due to decimal precision, so use `int` when you only need whole numbers.

## Type Casting

Converting a value to another data type is called **type casting**. There are two types:

- **Widening** goes from a smaller type to a larger one. Java does this automatically, because nothing is lost:
  - `byte` → `short` → `int` → `long` → `float` → `double`
  - `char` also widens to `int` (every character has a number)

  ```java
  int myInt = 12;
  double myDouble = myInt;
  System.out.println(myDouble); // 12.0
  ```

- **Narrowing** goes the other way. You must do it **manually** by putting the type you're converting to in parentheses in front of the value:

  ```java
  double myDouble = 12.5;
  int myInt = (int) myDouble;
  System.out.println(myInt); // 12 - the decimal is cut off, not rounded
  ```

## Naming Conventions

Use names that make your code readable and help avoid errors.

**Variables**
- Use **descriptive** names: `tP` → `totalPrice`
- Follow **camelCase**: lowercase first word, capitalize the first letter of every word after: `firstName`, `totalPrice`
- Keep names clear and concise
- Stick to a consistent naming style throughout your code

**Classes**
- Use nouns: `HelloWorld`, `Robot`
- Camel case, but with a **capital first letter**

**Methods**
- Use verbs: `getGrade`, `printTable`
- Follow camelCase

**Comments**
- Use comments sparingly. Good names make your code self-explanatory.

```java
// Single-line comment

/*
 * Multi-line comment
 */
```

## Getting Input from the User

So far our programs only output. To take **input**, Java gives us `Scanner`. You don't need to understand everything on these lines yet, just the pattern:

```java
import java.util.Scanner; // goes at the very top of the file

public class Greeting {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = input.nextLine();   // reads a whole line of text

        System.out.print("Enter your age: ");
        int age = input.nextInt();        // reads an int

        System.out.println("Hi " + name + ", you are " + age);
    }
}
```

- `input.nextInt()` reads an `int`
- `input.nextDouble()` reads a `double`
- `input.nextLine()` reads a line of text as a `String`

The `+` joins text and values together. We'll look at that more in Arithmetic Operators.

## Things to Think About

- What primitive data type would you use for the date of the month?
- What exactly could `double` be used for? What about `char`?
- Booleans are very useful for conditional statements, why is that?

## Review

- What's the difference between declaring and initializing a variable?
- Name the four primitive types we covered and what each holds.
- What happens to `9.99` when you cast it to an `int`?
- Which of these names follows Java conventions for a variable: `TotalPrice`, `total_price`, `totalPrice`?

## Exercises

- [Variables (Follow Along)](exercises/e01-variables-demo/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get variables-demo          # Variables (Follow Along)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get variables-and-data-types`.

Tip: keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.
