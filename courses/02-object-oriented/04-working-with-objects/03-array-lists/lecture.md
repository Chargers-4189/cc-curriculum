> **Objectives**
> - Make an `ArrayList` and add, get, change and remove items
> - Search an `ArrayList` with `contains` and `indexOf`
> - Loop over an `ArrayList`, including with a for-each loop
> - Store objects and wrapped primitives in an `ArrayList`
> - Choose between an array and an `ArrayList`
>
> **Prerequisites:** [Objects in Methods and Arrays](../02-objects-in-methods-and-arrays/lecture.md)

*Parts of this lesson are adapted from Head First Java (Sierra, Bates & Gee), Chapter 6, and Introduction to Java Programming (Liang), 11.11.*

## Follow Along

Write `ListsDemo.java` along with this lesson. Get the starter files in Charging Courses Labs with `ccm get arraylist-demo`. `Robot.java` is already done. Write each section's code under its matching `// --- Section ---` comment, and run it as you go.

## When Arrays Aren't Enough

Arrays have one big limit: **their size is fixed.** You have to know how big to make it when you create it. What if you're reading names until someone types `done`? Or adding robots to a team as people sign up? You don't know the size ahead of time.

Java comes with a class for this: **`ArrayList`**. It's a list that **grows and shrinks** as you add and remove things. It's part of the Java library, already written and ready to use, like `Scanner` and `Math`.

## Making an ArrayList

```java
import java.util.ArrayList;   // at the very top of the file, like Scanner

ArrayList<String> parts = new ArrayList<>();
System.out.println(parts.size());   // 0
```

- The type in the angle brackets, `<String>`, is what the list holds. `ArrayList<String>` means "a list of Strings." `ArrayList<Robot>` would be a list of robots.
- You don't give it a size. A new `ArrayList` starts empty.
- The `<>` on the right can be left empty: Java figures out the type from the left side.

`ArrayList` is just a class, and `parts` is a reference to an `ArrayList` object. Everything you do with it is a regular method call with the dot operator.

## Adding and Getting

```java
parts.add("motor");
parts.add("wheel");
parts.add("bumper");
System.out.println(parts);          // [motor, wheel, bumper]
System.out.println(parts.get(1));   // wheel
System.out.println(parts.size());   // 3
```

- `add(item)` puts it at the end. The list grows to make room.
- `get(index)` gives back the item at that index. Indexes start at 0, just like arrays.
- `size()` is how many items are in it. (Arrays use `.length`, ArrayLists use `.size()`.)
- Printing an ArrayList prints everything in brackets.

You can also squeeze an item in at an index. Everything after it moves down one:

```java
parts.add(1, "battery");
System.out.println(parts);   // [motor, battery, wheel, bumper]
```

## Changing and Removing

```java
parts.set(0, "falcon motor");   // replace the item at index 0
parts.remove("wheel");          // remove by value
parts.remove(0);                // remove by index
System.out.println(parts);      // [battery, bumper]
```

When you remove something, **everything after it shifts down** to fill the gap. No empty slots, no `null`. Try that with an array!

`remove(value)` gives back `true` if it found and removed the item, or `false` if it wasn't there.

> [!WARNING]
> Like arrays, `get`, `set` and `remove` with an index that doesn't exist crash with an `IndexOutOfBoundsException`. **Try it:** call `parts.get(5)`, read the error, then comment it out.

## Searching

```java
System.out.println(parts.contains("bumper"));   // true
System.out.println(parts.indexOf("bumper"));    // 1
System.out.println(parts.indexOf("camera"));    // -1: not in the list
System.out.println(parts.isEmpty());            // false
```

With an array, you'd have to write a loop for each of these. `ArrayList` already has them.

## Looping

The loop you know works, with `size()` and `get(i)`:

```java
for (int i = 0; i < parts.size(); i++) {
    System.out.println(i + ": " + parts.get(i));
}
```

When you don't need the index, use the **for-each** loop from [Objects in Methods and Arrays](../02-objects-in-methods-and-arrays/lecture.md#looping-over-objects). It works on ArrayLists the same way it works on arrays:

```java
for (String part : parts) {
    System.out.println("- " + part);
}
```

Each time through, `part` is the next item in the list. Same rule as with arrays: use for-each unless you need the index.

> [!TIP]
> Don't add or remove items inside a for-each loop. It usually crashes with a `ConcurrentModificationException`. If you need to remove while looping, use a regular `for` loop and go **backward**, from `size() - 1` down to `0`, so the items you haven't checked yet don't shift.

## ArrayLists of Objects

An `ArrayList` can hold any kind of object:

```java
ArrayList<Robot> team = new ArrayList<>();
team.add(new Robot("Bolt", 70));
team.add(new Robot("Volt", 100));

for (Robot r : team) {
    System.out.println(r.getName() + ": " + r.getBattery() + "%");
}
```

Just like an array of objects, the list holds **references**. `team.get(0)` gives back a reference to the Bolt robot, so `team.get(0).getName()` is `"Bolt"`.

## Primitives Need Wrappers

Can you make an `ArrayList<int>`? No. An `ArrayList` can only hold **objects**, and `int` is a primitive.

```java
ArrayList<int> scores = new ArrayList<>();       // won't compile
ArrayList<Integer> scores = new ArrayList<>();   // works
```

Every primitive has a **wrapper class** that's an object version of it: `Integer` for `int`, `Double` for `double`, `Boolean` for `boolean`, `Character` for `char`. Java converts back and forth for you, so you can mostly treat them like the primitives:

```java
scores.add(85);              // the int 85 gets wrapped into an Integer
int first = scores.get(0);   // and unwrapped back into an int
```

> [!WARNING]
> Watch out with `remove` on an `ArrayList<Integer>`. `scores.remove(1)` removes the item at **index** 1, not the number 1. To remove the value, use `scores.remove(Integer.valueOf(1))`.

## Arrays vs ArrayLists

| | Array | ArrayList |
|---|---|---|
| Make one | `String[] a = new String[10];` | `ArrayList<String> list = new ArrayList<>();` |
| Size | Fixed when it's made | Grows and shrinks |
| How many? | `a.length` | `list.size()` |
| Get | `a[i]` | `list.get(i)` |
| Change | `a[i] = "x";` | `list.set(i, "x");` |
| Add to the end | (make a bigger array and copy) | `list.add("x");` |
| Remove | (shift everything yourself) | `list.remove(i);` |
| Holds primitives? | Yes: `int[]` | Only wrapped: `ArrayList<Integer>` |

Use an **array** when the size is fixed and known, like the 6 matches in a schedule or the 4 wheels on a drivetrain. Use an **ArrayList** when things get added and removed as the program runs.

## Review Quiz

[ArrayList Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Shopping List

[Shopping List](exercises/e02-shopping-list/prompt.md)

### 2. Remove the Negatives

[Remove the Negatives](exercises/e03-remove-the-negatives/prompt.md)

## Homework

### Team Roster

[Team Roster](exercises/e04-team-roster/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 6: Using the Java Library (pp. 132 to 137)
- Introduction to Java Programming (Liang), 11.11: The ArrayList Class
- [ArrayList](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html), the official Java documentation (every method it has)
