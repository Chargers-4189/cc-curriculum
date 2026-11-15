> **Objectives**
> - Repeat code with a `while` loop
> - Name the two things every loop needs
> - Build a loop step by step with the 3-step recipe
> - Use a sentinel value to stop a loop when you don't know the count
>
> **Prerequisites:** [If Statements](../../04-conditionals/01-if-statements/lecture.md): conditions and booleans

## Follow Along

Write `While.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get while-demo` and open `While.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one.

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

> [!WARNING]
> **Try it:** delete the `i++` from your loop and run it. It never ends! Click into the terminal and press **Ctrl + C** to stop it. Then **put the `i++` back**, or your program will get stuck there every time you run it.

## How to Write a Loop: The 3-Step Recipe

Don't try to write the finished loop in one go. Instead:

1. Write the code to do the thing **once**. Get it working.
2. Wrap it in `while (true) { ... }`
3. Replace `true` with a real condition, and add whatever statement makes that condition eventually become false.

## Sentinel-Controlled Loops

Sometimes you **don't know** how many times to loop, because the user decides. A **sentinel** is a special value that means "I'm done".

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

## Review Quiz

[While Loops Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Countdown

[Countdown](exercises/e02-countdown/prompt.md)

### 2. Count the Digits

[Count the Digits](exercises/e03-count-the-digits/prompt.md)

### 3. Average Until -1

[Average Until -1](exercises/e04-average-until-sentinel/prompt.md)

## Homework

### Guess the Number

[Guess the Number](exercises/e05-guess-game/prompt.md)
