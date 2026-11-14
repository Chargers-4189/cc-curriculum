> **Objectives**
> - Write `for` loops and trace their order of execution
> - Count up, count down, and count by steps
> - Nest loops to work with rows and columns
> - Use `break` and `continue`
> - Choose between `for` and `while`
>
> **Prerequisites:** [While Loops](../01-while-loops/lecture.md)

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

## Review

- In what order do the three parts of a for loop's header run?
- What does `for (int k = 10; k > 0; k -= 2)` print?
- In a nested loop, how many times does the inner body run if the outer loop runs 5 times and the inner loop runs 3 times?
- What's the difference between `break` and `continue`?

## Exercises

- [Loops (Follow Along)](exercises/e01-loops-demo/prompt.md)
- [Number Pyramid (Homework)](exercises/e02-number-pyramid/prompt.md)
- [Leap Years (Homework)](exercises/e03-leap-years/prompt.md)

### Getting the Files

Open a terminal in your workspace and run:

```bash
ccm get loops-demo              # Loops (Follow Along)
ccm get number-pyramid          # Number Pyramid (Homework)
ccm get leap-years              # Leap Years (Homework)
```

Each command creates a folder with that exercise's starter code. To get the whole lesson at once, including every exercise, run `ccm get for-loops`.

> [!TIP]
> Keep your downloads organized by running these inside a folder like `fundamentals`, `week1`, or `hwk` (`mkdir -p fundamentals/hwk`, then `cd` into it). See [Java Workspace](../../01-getting-started/04-java-workspace/lecture.md#keep-your-downloads-organized) for an example.

To check homework, run `ccm test` from inside its folder:

```bash
cd number-pyramid
ccm test
```
