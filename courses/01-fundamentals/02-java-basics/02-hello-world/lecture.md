---
title: "Hello World"
prerequisites: [how-java-works]
---

# Hello World

> **Objectives**
> - Write, compile, and run your first Java program
> - Use `System.out.println` to output to the console
> - Know why the file name and class name must match
>
> **Prerequisites:** [How Java Works](../01-how-java-works/lecture.md): source files, classes, and the `main` method

## Creating Your First Program

Let's create a simple Hello World program. It has three parts:

- **Class declaration:** `public class HelloWorld { ... }`
  - We're creating a class called `HelloWorld`
- **Main method:** `public static void main(String[] args) { ... }`
  - Using the main method to start
- **Print to console:** `System.out.println("Hello World");`
  - Prints a line of text as output

Create a file called `HelloWorld.java` and type:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

Run it and you should see:

```
Hello World
```

## Breaking It Down

- Notice how our **file name and class name are the same**: `HelloWorld.java` holds `class HelloWorld`.
  - This keeps your code **organized** and makes your classes **easier** to find and understand.
  - This is a **strict rule** for public classes. If they don't match, Java won't compile it:

    ```
    error: class HelloWorld is public, should be declared in a file named HelloWorld.java
    ```
- `System.out.println` is a form of **output** in Java. It prints whatever is in the parentheses, then moves to a new line.
  - `System.out.print` (no `ln`) prints without moving to a new line.
  - Text goes inside double quotes: `"Hello World"`. This is called a **String**.
- The **main method** is our only method, and all our code is within it.
- Every statement ends with a **semicolon** `;`

## Common Mistakes

Java is very picky. Watch out for:

- A missing semicolon: `System.out.println("Hello World")` won't compile
- Capitalization: `system.out.println` or `Main` vs `main` are different names to Java
- Missing or extra curly braces `{ }`. Every opening brace needs a closing brace.
- Forgetting the quotes around text

When something goes wrong, read the error! It tells you the file, the line number, and what Java expected.

## Things to Think About

- Why would it be important for your code to be readable?
- What do you think could be another output form?
- What is the purpose of `main`? Why is it necessary for any Java program?
- Every statement in Java must end with what?

## Review

- What three parts does every Hello World program have?
- What happens if the file name and the public class name don't match?
- What's the difference between `print` and `println`?

## Exercises

- [Hello World (Follow Along)](exercises/e01-hello-demo/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get hello-demo              # Hello World (Follow Along)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get hello-world`.

Tip: keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.
