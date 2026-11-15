> **Objectives**
> - Declare and initialize variables
> - Choose the right data type: `int`, `double`, `char`, `boolean`, `String`
> - Convert between types with type casting
> - Name variables, methods, and classes using Java conventions
> - Read input from the user with `Scanner`
>
> **Prerequisites:** [Hello World](../02-hello-world/lecture.md): writing and running a program

## Follow Along

In this lesson you'll write `Variables.java` along with us. Open a terminal in **Charging Courses Labs** and run:

```bash
mkdir -p fundamentals/week1
cd fundamentals/week1
ccm get variables-demo
cd variables-demo
```

Then open `Variables.java` from the Explorer. It has a comment for each section of this lesson, like `// --- Type Casting ---`, so you know where each part goes. As you go through the lesson, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one. Type it out yourself instead of copying and pasting.

> [!TIP]
> Keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.

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

> [!WARNING]
> **Try it:** add `age = "seventeen";` and run it. Java won't compile it, because `age` can only hold an `int`. Read the error, then **comment that line out** (put `//` in front of it) so the rest of your file runs.

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

> [!INFO]
> Consider size and memory when choosing data types. `int` is more efficient than `double` due to decimal precision, so use `int` when you only need whole numbers.

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

## Review Quiz

[Variables and Data Types Quiz](quiz/review.csv)

## Practice

Each problem below has a code editor right on this page. Write your code, click **Test Run**, and keep going until every test passes.

> [!INFO]
> When the tests run, nobody is typing, so the input doesn't show up in your output. That's why an expected output looks like `Enter your name: Enter your age: Hi Ada, you are 15`, with the prompts squished onto one line. Your program is fine; just make sure your prompts match the starter code exactly.

> [!TIP]
> Rather work in Labs? Each problem has a `ccm get` command under it. Write your code in `Main.java` and check it with `ccm test`.

### 1. Greeting

[Greeting](exercises/e02-greeting/prompt.md)

### 2. Whole Part

[Whole Part](exercises/e03-whole-part/prompt.md)

### 3. Swap Two Values

[Swap Two Values](exercises/e04-swap-values/prompt.md)
