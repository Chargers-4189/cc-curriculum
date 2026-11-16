> **Objectives**
> - Name the four pillars of object-oriented programming
> - Explain the difference between a class and an object
> - Design a class from what it knows (instance variables) and what it does (methods)
> - Make objects with `new` and use them with the dot operator
>
> **Prerequisites:** [Shape Wars](../../01-introduction-to-oop/02-shape-wars/lecture.md)

*Parts of this lesson are adapted from Head First Java (Sierra, Bates & Gee), Chapter 2.*

## Follow Along

Write `Cat.java` and `CatTester.java` along with this lesson. Get the starter files in Charging Courses Labs with `ccm get cat-demo`. Each file has `// --- Section ---` comments that match the headings in this lesson, so write each section's code under its matching comment. Run `CatTester`, since it's the one with `main`.

## Where We Left Off

In Shape Wars we looked at two ways of programming. Team A wrote **procedural** code, which is how you've been writing programs so far: a `main` and a bunch of methods. Team B wrote **object-oriented** code, with a class for each shape. You also got a quick look at classes, methods, instance variables, inheritance and overriding.

```
            Shape
          rotate()
        playSound()
              |
   +------+---+---+------+
 Square Circle Triangle Amoeba
                       rotate()      <- overrides
                       playSound()   <- overrides
```

We'll build on all of that over the next few weeks, but first we need to get comfortable with classes and objects.

## The Four Pillars

Object-oriented programming is built on four main ideas. We'll go through each of them in this course:

| Pillar | In short |
|---|---|
| **Encapsulation** | An object keeps its data to itself and controls how it changes |
| **Inheritance** | A class can take what another class already has (like `Shape` and `Amoeba`) |
| **Polymorphism** | One type, many forms: every `Shape` can `rotate()`, each in its own way |
| **Abstraction** | Only show what you need to use something, hide the details |

You don't need to know these yet. Just know the names, you'll hear them a lot.

## Classes and Objects

A **class** is a blueprint for making objects. It tells Java how to make an object of that type.

A **class is not an object.** Think of a blueprint for a house: you can't live in the blueprint, but you can build as many houses from it as you want. Each house can have its own paint color.

Same with classes: there's one `Cat` class, and every cat made from it can have its own name and color.

## What an Object Knows

When you design a class, think about two things. First: what does the object need to **know** about itself?

Things an object knows are called **instance variables**. Each object (each **instance** of the class) gets its own copy.

```java
public class Cat {
    String name;
    String color;
    String breed;
    double size;
}
```

Notice these don't have values. The class is just the blueprint, and we don't know which cat we're making yet. Each cat gets its own values when it's made.

## What an Object Does

Second: what can the object **do**? Things an object does are its **methods**.

```java
public class Cat {
    String name;
    String color;
    String breed;
    double size;

    void meow() {
        System.out.println("Meow");
    }

    void walk(double pace) {
        System.out.println(name + " is walking at pace " + pace);
    }

    void sleep() {
        System.out.println(name + " is asleep");
    }
}
```

These methods don't have `static` in front of them. A `static` method belongs to the class, like the ones you wrote in Fundamentals. These belong to **each cat**, so `walk` can use that cat's `name`.

Let's try a few more. For each one, what does it know, and what does it do?

| | Knows (instance variables) | Does (methods) |
|---|---|---|
| **Car** | speed, seats, color, year, engine | move, park, reverse |
| **Shopping Cart** | material, cart contents | add item, remove item, check out |
| **Alarm** | time, alarm time, ringtone, mode | ring, set time, set alarm, snooze, turn off |
| **Button** | label, color | push, release |

Look at the button. One `Button` class can make a "Backspace" button that's pink, a "Nuclear launch" button that's red, and an "A" button that's green. Same blueprint, different values.

> [!TIP]
> It's common for an object to have methods that read or change its own instance variables. An alarm's `setAlarm` method changes its alarm time, and `ring` uses its ringtone.

## Making an Object

To use a class, you need a second class with a `main` method. We'll call it a **tester** class. `Cat.java` is the blueprint, and `CatTester.java` is where we make cats and use them.

```java
public class CatTester {
    public static void main(String[] args) {
        Cat myCat;          // a variable that can hold a Cat (nothing in it yet)
        myCat = new Cat();  // make a Cat object
    }
}
```

`new Cat()` makes a brand new `Cat` object. Usually you do both on one line:

```java
Cat myCat = new Cat();
```

The variable's type is `Cat`. The class you write becomes a type, just like `int` or `String`.

## The Dot Operator

The **dot operator** (`.`) gives you access to an object's instance variables and methods.

```java
myCat.meow();               // tell the cat to meow
myCat.name = "Mr. Trinity"; // set its name
myCat.walk(1.0);            // Mr. Trinity is walking at pace 1.0
```

Read `myCat.meow()` as "use the cat in `myCat` to call `meow()`".

> [!WARNING]
> **Try it:** in `CatTester`, call `Cat.meow();` (using the class name instead of your variable). It won't compile: `meow` belongs to a cat, so you have to say **which** cat. Read the error, then comment it out.

## Every Object Gets Its Own Values

Make a second cat:

```java
Cat otherCat = new Cat();
otherCat.name = "Mochi";
otherCat.walk(2.5);   // Mochi is walking at pace 2.5
myCat.sleep();        // Mr. Trinity is asleep
```

Both cats run the **same** `walk` method, but each one uses its own `name`. Changing `otherCat.name` does nothing to `myCat`.

## Review Quiz

[Objects Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

In the editor everything goes in one file, `Main.java`. The class with `main` is `public class Main`, and the other classes go below it **without** `public`.

### 1. Two Cats

[Two Cats](exercises/e02-two-cats/prompt.md)

### 2. Button Class

[Button Class](exercises/e03-button-class/prompt.md)

## Homework

### Movie Class

[Movie Class](exercises/e04-movie-class/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 2: A Trip to Objectville
- Introduction to Java Programming (Liang), 9.1 to 9.3: Defining Classes for Objects
