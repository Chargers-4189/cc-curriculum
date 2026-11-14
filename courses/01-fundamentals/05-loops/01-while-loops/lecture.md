> **Objectives**
> - Repeat code with a `while` loop
> - Name the two things every loop needs
> - Build a loop step by step with the 3-step recipe
> - Use a sentinel value to stop a loop when you don't know the count
>
> **Prerequisites:** [If Statements](../../04-conditionals/01-if-statements/lecture.md): conditions and booleans

## Why Loops?

What if we needed to display "Welcome to Java!" a hundred times? It would be tedious to write the same statement a hundred times:

```java
System.out.println("Welcome to Java!");
System.out.println("Welcome to Java!");
System.out.println("Welcome to Java!");
// ...97 more
```

Java provides us with a construct called a **loop**. You can use it to tell the computer to repeat a section of code as many times as you need.

## The while Loop

Loops run by checking a **condition**. A `while` loop runs everything in its loop block **as long as the condition is true**. The loop block is defined by curly brackets `{ }`.

```java
while (loop-continuation-condition) {
    // loop body
}
```

1. The condition is checked
2. If it's `true`, the body runs, then go back to step 1
3. If it's `false`, the loop ends and the program continues after it

```java
int sum = 0, i = 1;
while (i < 10) {
    sum += i;
    i++;
}
System.out.println(sum); // 45
```

## The Two Things Every Loop Needs

1. **Something inside the body that changes**
2. **A condition that eventually becomes false because of that change**

In the example, `i++` changes `i`, and eventually `i < 10` becomes false. Forget the `i++` and `i` stays 1 forever. That's an **infinite loop**: the program never stops. (Stop it with **Ctrl + C** in the terminal.)

## How to Write a Loop: The 3-Step Recipe

Don't try to write the finished loop in one go. Instead:

1. Write the code to do the thing **once**. Get it working.
2. Wrap it in `while (true) { ... }`
3. Replace `true` with a real condition, and add whatever statement makes that condition eventually become false.

## Sentinel-Controlled Loops

Sometimes you **don't know** how many times to loop. The user decides. A **sentinel** is a special value that means "I'm done", not real data.

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter an integer (ends if it is 0): ");
int data = input.nextInt();

int total = 0;
while (data != 0) {
    total += data;
    System.out.print("Enter an integer (ends if it is 0): ");
    data = input.nextInt();
}
System.out.println("Sum is " + total);
```

Here `0` is the sentinel. There's no counter at all.

- We read once **before** the loop and again at the **bottom** of the loop
- If the very first input is 0, the body never runs and the sum stays 0

## Case Study: Guess the Number

The computer picks a number from 0 to 100, and the user keeps guessing until they get it:

```java
int number = (int) (Math.random() * 101); // 0 to 100
Scanner input = new Scanner(System.in);

int guess = -1;
while (guess != number) {
    System.out.println("Enter your guess: ");
    guess = input.nextInt();

    if (guess > number) {
        System.out.println("Try again, too high");
    } else if (guess < number) {
        System.out.println("Try again, too low");
    }
}
System.out.println("You win!");
```

Why does `guess` start at `-1` and not `0`? Because `0` is a legal answer! If `guess` started at 0 and the secret number happened to be 0, the loop would never run. Pick a starting value that **can't be a real value**.

## Further

**do-while** checks the condition **after** the body, so the body always runs **at least once**:

```java
int value;
int total = 0;
do {
    System.out.print("Enter an integer (ends if it is 0): ");
    value = input.nextInt();
    total += value;
} while (value != 0);
System.out.println("Sum is " + total);
```

This is the sentinel program again, but the read appears only once. Use do-while for menus and prompts, anything that has to happen at least once. Don't forget the **semicolon** after `while (...)`.

## Review

- What two things does every loop need?
- What happens if a loop's condition never becomes false?
- What is a sentinel value? Give an example.
- In the guessing game, why does `guess` start at `-1`?

## Exercises

- [Guess the Number](exercises/e01-guess-game/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get guess-game              # Guess the Number
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get while-loops`.

> [!TIP]
> Keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.
