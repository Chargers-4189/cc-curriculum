> **Objectives**
> - Create an array and access its elements by index
> - Use `.length` to find how many elements an array has
> - Loop through an array with a `for` loop
> - Recognize an out-of-bounds error
>
> **Prerequisites:** [For Loops](../../05-loops/02-for-loops/lecture.md)

## Follow Along

Write `ArraysDemo.java` along with this lesson. Get the starter file in Charging Courses Labs with `ccm get arrays-demo` and open `ArraysDemo.java`. It has a `// --- Section ---` comment for each heading in this lesson. As you go, write each section's code (and any notes you want, as `//` comments) under its matching comment, then run it. If a variable name is already taken earlier in your file, just pick a new one.

## What is an Array?

Say you want to store 30 test scores. You could make 30 variables: `score1`, `score2`, `score3`... but that gets out of hand fast.

**Arrays** are just a tray of containers. They hold **many values of the same type** under one name, and you use an **index position** to get to any element in the array.

- Every element in an array is just a variable
- An array has a **fixed size**: once it's created, it can't grow or shrink

## Creating an Array

If you already know the values, list them in curly braces:

```java
int[] scores = {90, 85, 72, 100, 64};
String[] names = {"Ada", "Grace", "Alan"};
```

If you only know the size, create an empty one with `new`:

```java
double[] temperatures = new double[7]; // 7 slots, all starting at 0.0
```

- The `[]` after the type means "array of"
- Empty arrays start filled with a default value: `0` for numbers, `false` for booleans

## Indexes

Each element has an **index**, its position in the array. Indexes **start at 0**:

```
index:    0    1    2    3    4
scores: [90] [85] [72] [100] [64]
```

```java
System.out.println(scores[0]); // 90 - the first element
System.out.println(scores[4]); // 64 - the last element
scores[2] = 75;                // change the third element
```

## Length

`.length` tells you how many elements an array has:

```java
System.out.println(scores.length);                // 5
System.out.println(scores[scores.length - 1]);   // 64 - always the last element
```

Since indexes start at 0, the last index is always `length - 1`.

## Out of Bounds

Using an index that doesn't exist crashes the program:

```java
System.out.println(scores[5]); // ArrayIndexOutOfBoundsException
```

`scores` has 5 elements, so the valid indexes are 0 to 4.

> [!WARNING]
> **Try it:** under `// --- Out of Bounds ---`, add `System.out.println(scores[5]);` and run it. Read the crash, then **comment it out**, or the rest of your program won't run.

## Looping Through an Array

Arrays and for loops go together. Loop from `0` up to (but not including) `length`:

```java
for (int i = 0; i < scores.length; i++) {
    System.out.println("Score " + i + ": " + scores[i]);
}
```

This works for any size array. Two common patterns:

```java
// Sum and average
int sum = 0;
for (int i = 0; i < scores.length; i++) {
    sum += scores[i];
}
double average = (double) sum / scores.length;

// Highest value
int max = scores[0];
for (int i = 1; i < scores.length; i++) {
    if (scores[i] > max) {
        max = scores[i];
    }
}
```

Notice `i < scores.length`, not `<=`. Using `<=` would go one past the end.

## Arrays Are Objects

You'll hear that arrays are always **objects**, whether they hold primitives or not. That's why we create them with `new` and why `.length` uses a dot. We'll dig into what that means in the Object Oriented course. For now, you know everything you need to use them.

## Review Quiz

[Arrays Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Reverse the List

[Reverse the List](exercises/e02-reverse-the-list/prompt.md)

### 2. Min and Max

[Min and Max](exercises/e03-min-and-max/prompt.md)

### 3. Above Average

[Above Average](exercises/e04-above-average/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 3: Know Your Variables ("An array is like a tray of cups")
- Introduction to Java Programming (Liang), 7.1 to 7.3: Array Basics and the Analyzing Numbers case study
