> **Objectives**
> - Write, compile, and run your first Java program
> - Use `System.out.println` to output to the console
> - Know why the file name and class name must match
>
> **Prerequisites:** [How Java Works](../01-how-java-works/lecture.md): source files, classes, and the `main` method

## Follow Along

You'll write your first program, `HelloWorld.java`, in **Charging Courses Labs** (your workspace from [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md)). Open VS Code, open a terminal, and run:

```bash
mkdir -p fundamentals/week1
cd fundamentals/week1
ccm get hello-demo
cd hello-demo
```

This downloads a folder called `hello-demo` with a starter `HelloWorld.java` inside. Open it from the Explorer on the left.

Work through the lesson one section at a time. Type each example into `HelloWorld.java` and click **Run** (▷). Type the code out instead of copying and pasting.

> [!TIP]
> Keep downloads organized in folders like `fundamentals/week1` and `fundamentals/hwk`. See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized).

## Creating Your First Program

Let's create a simple Hello World program. It has three parts:

- **Class declaration:** `public class HelloWorld { ... }`
  - We're creating a class called `HelloWorld`
- **Main method:** `public static void main(String[] args) { ... }`
  - Using the main method to start
- **Print to console:** `System.out.println("Hello World");`
  - Prints a line of text as output

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

Now try it from the terminal too. This is the compiler and the runtime from [How Java Works](../01-how-java-works/lecture.md):

```bash
javac HelloWorld.java
java HelloWorld
```

## Breaking It Down

- Notice how our **file name and class name are the same**: `HelloWorld.java` holds `class HelloWorld`.
  - This is a **strict rule** for public classes. If they don't match, Java won't compile it:

    ```
    error: class HelloWorld is public, should be declared in a file named HelloWorld.java
    ```
- `System.out.println` is a form of **output** in Java. It prints whatever is in the parentheses, then moves to a new line.
  - `System.out.print` (no `ln`) prints without moving to a new line.
  - Text goes inside double quotes: `"Hello World"`. This is called a **String**.
- The **main method** is our only method, and all our code is within it.
- Every statement ends with a **semicolon** `;`

```java
System.out.print("Hello ");
System.out.print("from ");
System.out.println("Java!");
System.out.println("This is on a new line.");
```

> [!TIP]
> **Try it:** change `public class HelloWorld` to `public class Hello` and run it. You'll get the error above. Change it back.

## Common Mistakes

Java is very picky. Watch out for:

- A missing semicolon: `System.out.println("Hello World")` won't compile
- Capitalization: `system.out.println` or `Main` vs `main` are different names to Java
- Missing or extra curly braces `{ }`. Every opening brace needs a closing brace.
- Forgetting the quotes around text

When something goes wrong, read the error! It tells you the file, the line number, and what Java expected.

> [!WARNING]
> **Try it:** make one of the mistakes above, run it, and read the error. Fix it before trying the next one.

## Things to Think About

- Why would it be important for your code to be readable?
- What do you think could be another output form?
- What is the purpose of `main`? Why is it necessary for any Java program?
- Every statement in Java must end with what?

## Review Quiz

[Hello World Quiz](quiz/review.csv)

## Practice

Each problem has a code editor on this page. Write your code and click **Test Run** until every test passes. Keep the class named `Main`.

> [!TIP]
> To work in Labs instead, use the `ccm get` command under each problem and check your code with `ccm test`.

### 1. Three Lines

[Three Lines](exercises/e02-three-lines/prompt.md)

### 2. Fix the Bugs

[Fix the Bugs](exercises/e03-fix-the-bugs/prompt.md)

### 3. Robot Face

[Robot Face](exercises/e04-robot-face/prompt.md)
