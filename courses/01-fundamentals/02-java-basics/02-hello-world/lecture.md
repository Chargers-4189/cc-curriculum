> **Objectives**
> - Write, compile, and run your first Java program
> - Use `System.out.println` to output to the console
> - Know why the file name and class name must match
>
> **Prerequisites:** [How Java Works](../01-how-java-works/lecture.md): source files, classes, and the `main` method

## Follow Along

In this lesson you'll write your first program, `HelloWorld.java`, right along with us. You'll do this in **Charging Courses Labs** (your workspace from [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md)). Open VS Code, open a terminal, and run:

```bash
mkdir -p fundamentals/week1
cd fundamentals/week1
ccm get hello-demo
cd hello-demo
```

This downloads a folder called `hello-demo` with a starter `HelloWorld.java` inside. Open it from the Explorer on the left.

Work through the lesson one section at a time. Type each example into `HelloWorld.java` and run it with **Run** (▷). Add notes as `//` comments if they help. Type the code out yourself instead of copying and pasting. It's how you learn it!

> [!TIP]
> Keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.

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

```java
System.out.print("Hello ");
System.out.print("from ");
System.out.println("Java!");
System.out.println("This is on a new line.");
```

> [!TIP]
> **Try it:** change `public class HelloWorld` to `public class Hello` and run it. You'll get the error above. Change it back before moving on, or nothing else will run!

## Common Mistakes

Java is very picky. Watch out for:

- A missing semicolon: `System.out.println("Hello World")` won't compile
- Capitalization: `system.out.println` or `Main` vs `main` are different names to Java
- Missing or extra curly braces `{ }`. Every opening brace needs a closing brace.
- Forgetting the quotes around text

When something goes wrong, read the error! It tells you the file, the line number, and what Java expected.

> [!WARNING]
> **Break it on purpose:** make one of the mistakes above in your file, run it, and read the error. Then **fix it before trying the next one**. If you leave a mistake in, your program won't run at all, even the parts that were fine.

## Things to Think About

- Why would it be important for your code to be readable?
- What do you think could be another output form?
- What is the purpose of `main`? Why is it necessary for any Java program?
- Every statement in Java must end with what?

## Review Quiz

[Hello World Quiz](quiz/review.csv)

## Practice

Time to practice on your own! Each problem below has a code editor right on this page:

1. Read the task, then write your code in the editor.
2. Click **Test Run**. Each test shows what your program should print and what it actually printed.
3. Keep going until every test passes.

Practice problems always use a class named `Main`, because the editor runs your code as `Main.java`. Keep the class name as `Main` (the file name rule from above!).

> [!TIP]
> Rather work in your workspace? Each problem also has a `ccm get` command. Download it in Charging Courses Labs, write your code in `Main.java`, and check it with `ccm test`.

### 1. Three Lines

[Three Lines](exercises/e02-three-lines/prompt.md)

### 2. Fix the Bugs

[Fix the Bugs](exercises/e03-fix-the-bugs/prompt.md)

### 3. Robot Face

[Robot Face](exercises/e04-robot-face/prompt.md)
