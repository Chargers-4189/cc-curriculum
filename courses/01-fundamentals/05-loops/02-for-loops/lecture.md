> **Objectives**
> - Write `for` loops and trace their order of execution
> - Count up, count down, and count by steps
> - Nest loops to work with rows and columns
> - Use `break` and `continue`
> - Choose between `for` and `while`
>
> **Prerequisites:** [While Loops](../01-while-loops/lecture.md)

## Follow Along

Write `ForLoops.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get for-demo` and open `ForLoops.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one.

## Same Loop, One Line

Every counting while loop has the same three parts, scattered across three different places:

```java
int k = 0;          // initialization (above the loop)
while (k < 10) {    // condition
    // ...
    k++;            // update (buried at the bottom, easy to forget)
}
```

A `for` loop puts all three in the header where you can see them:

```java
for (int k = 0; k < 10; k++) {
    System.out.println("Welcome to Java!");
}
```

- **Initialize** - declare the loop variable
- **Conditional test** - results in a boolean; the loop runs while it's true
- **Iteration expression** - what to do after each pass, usually `k++`

The loop block is defined by curly brackets `{ }`.

![The parts of a for loop](assets/slide-for-loop.png)

## Order of Execution

1. The initialization runs **once**
2. The condition is checked. If `false`, stop
3. The body runs
4. The update runs
5. Go back to step 2

```
for ([1]; [2]; [4]) {
    [3];
}
```

A variable declared in the header **only exists inside the loop**. After the loop ends, `k` is gone.

> [!WARNING]
> **Try it:** under `// --- Order of Execution ---`, write a loop from 0 to 2 that prints `"k is " + k`. Then add `System.out.println(k);` **after** the loop. It won't compile, because `k` is gone. Read the error, then comment that line out.

## Counting Different Ways

```java
for (int k = 5; k >= 1; k--) {
    System.out.print(k + " ");     // 5 4 3 2 1
}

for (int k = 0; k <= 20; k += 5) {
    System.out.print(k + " ");     // 0 5 10 15 20
}
```

Watch out for **off-by-one** errors: `n <= 10` runs ten times starting at 1, `n < 10` runs nine.

## Which Loop Should I Use?

- **for** → I know how many times ("print 10 rows", "1 to 100")
- **while** → I don't ("until the user types 0", "until they guess it")

Any loop can be written either way. Pick the one that makes the code readable.

## Nested For Loops

A loop inside a loop. The **outer** loop picks a **row**, and the **inner** loop fills that row with **columns**:

```java
for (int row = 1; row <= 9; row++) {
    System.out.print(row + " | ");
    for (int col = 1; col <= 9; col++) {
        System.out.printf("%4d", row * col);
    }
    System.out.println();
}
```

```
1 |    1   2   3   4   5   6   7   8   9
2 |    2   4   6   8  10  12  14  16  18
3 |    3   6   9  12  15  18  21  24  27
...
```

- The inner loop runs start to finish for **every** pass of the outer loop: 9 × 9 = 81 numbers
- The `println()` at the end of the outer loop is what ends each row
- `printf("%4d", value)` prints a number in a space 4 characters wide, which lines the columns up

Be careful: nesting multiplies. Three nested loops of 10,000 each is a **trillion** iterations.

## break and continue

- `break` - get out of the loop entirely, right now
- `continue` - skip the **rest** of this pass and go to the next one

```java
// break: stop once the sum reaches 100
int bSum = 0;
for (int n = 1; n <= 20; n++) {
    bSum += n;
    if (bSum >= 100) {
        break;
    }
}
System.out.println("Stopped at sum = " + bSum); // 105

// continue: add only the odd numbers
int cSum = 0;
for (int n = 1; n <= 20; n++) {
    if (n % 2 == 0) {
        continue; // skip the even numbers
    }
    cSum += n;
}
System.out.println("Sum of odds = " + cSum); // 100
```

Both are conveniences; you could use a boolean flag instead. Be wary of using lots of `break`s, since multiple exits make a loop hard to follow. In a nested loop, `break` only exits the **inner** loop.

## Review Quiz

[For Loops Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Multiples

[Multiples](exercises/e02-multiples/prompt.md)

### 2. Factorial

[Factorial](exercises/e03-factorial/prompt.md)

### 3. Star Triangle

[Star Triangle](exercises/e04-star-triangle/prompt.md)

## Homework

### Number Pyramid

[Number Pyramid](exercises/e05-number-pyramid/prompt.md)

### Leap Years

[Leap Years](exercises/e06-leap-years/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 5: Extra-Strength Methods ("More about for loops")
- Introduction to Java Programming (Liang), 5.7 to 5.9: the for loop, which loop to use, and nested loops, and 5.12: Keywords break and continue
