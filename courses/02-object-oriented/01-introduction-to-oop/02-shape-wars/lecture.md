> **Objectives**
> - Keep a working program working while the spec changes
> - Compare procedural code with object-oriented code
> - Explain what an object knows and what it does
> - Tell a class apart from an object
>
> **Prerequisites:** [Writing Methods](../../../01-fundamentals/07-methods/01-writing-methods/lecture.md)

*Shape Wars is adapted from "Chair Wars" in Head First Java (Sierra, Bates & Gee), Chapter 2.*

## Follow Along

The class splits into two teams. Each team only gets its own team's file, so don't go looking at the other one.

- **Team A:** `ccm get shape-wars-team-a`, then open `TeamA.java`
- **Team B:** `ccm get shape-wars-team-b`, then open `TeamB.java`

Run it with `java TeamA.java` (or `java TeamB.java`), or use the Run button.

## The Setup

Two teams were given the same spec and built the same program two different ways. Both work. Both are done. Both are tested. Your job is to keep them working while the client changes their mind.

Run your program. Both teams get the same output:

```
--- user clicked the square ---
Rotating the square 360 degrees around (25.0, 25.0)
Playing square.wav
...
```

**This isn't a race.** Your score is **how many lines of already-working code you had to touch.** A new class or a new file costs 0. Changing a line that already worked costs 1. Lowest score wins.

| | Spec change 1 | Spec change 2 | Total lines touched |
|---|---|---|---|
| Team A | | | |
| Team B | | | |

## Read Your Own Code

Before any changes, answer these on paper:

1. If you wanted to know everything about the circle, where would you look?
2. Where does a shape's width live?

Hold on to your answers, we'll come back to them.

## Spec Change 1

> **Spec Change 1**
> There will be an amoeba shape on the screen with the others. When the user clicks it, it rotates like the others and plays an **.mp3** sound file instead of a .wav. It'll be no problem for programmers like you.

The amoeba is 35 wide and 20 tall. Make the change, then count your lines.

If you missed it in class, or want to try the other team's side, here are both:

### Team A

[Spec Change 1: Team A](exercises/e03-spec-change-1-team-a/prompt.md)

### Team B

[Spec Change 1: Team B](exercises/e04-spec-change-1-team-b/prompt.md)

## Spec Change 2

> **Spec Change 2**
> Oh, no. That's not how the amoeba is supposed to rotate. The others spin around their center. The amoeba spins around a point at **one end**, like a clock hand. The amoeba's rotation point is (0, 10).

Same deal: make the change and count your lines.

### Team A

[Spec Change 2: Team A](exercises/e05-spec-change-2-team-a/prompt.md)

### Team B

[Spec Change 2: Team B](exercises/e06-spec-change-2-team-b/prompt.md)

## What Happened

**Team A** wrote their program as a set of methods. Each method has a `switch` with a case for every shape. To add the amoeba, they had to edit `getName`, `getWidth`, `getHeight` and `playSound`, add a constant, and add it to the clicks. None of those edits are hard, but every one of them is a chance to break the square, which was working fine.

Then Spec Change 2 hurts. `rotate(int shapeNum)` has nowhere to put a rotation point. Team A has two options, and neither is good:

- Add an `if (shapeNum == AMOEBA)` inside `rotate`. It works, but now `rotate` has amoeba trivia in it, and the next weird shape adds another `if`.
- Change it to `rotate(int shapeNum, double xPt, double yPt)`. Now **every call** to `rotate` breaks, even the ones for shapes that were fine.

**Team B** wrote a class for each shape. To add the amoeba, they wrote one new class and a few lines in `main`. For Spec Change 2, the amoeba already knows things about itself, so it can know its own rotation point too:

```java
class Amoeba {
    double width = 35;
    double height = 20;
    double xPoint = 0;    // the amoeba's own rotation point
    double yPoint = 10;

    void rotate() {
        System.out.println("Rotating the amoeba 360 degrees around ("
                + xPoint + ", " + yPoint + ")");
    }

    void playSound() {
        System.out.println("Playing amoeba.mp3");
    }
}
```

Two new variables and one method body, all inside a class that was already new. `Square`, `Circle` and `Triangle` didn't get touched once.

Now go back to your answers from before. Where does a circle's width live? For Team A, it's spread across a bunch of `switch` statements. For Team B, it's in the `Circle` class, where everything about a circle belongs.

## Team A Fights Back

Team B isn't perfect either. Look at their four classes. What's wrong?

`rotate()` and `playSound()` are written **four times**. That's duplicate code, the exact thing we wrote methods to get rid of. Team A is right about this one.

The fix is **inheritance**. Pull what all four shapes have in common into one `Shape` class, and have each shape **inherit** from it. The amoeba rotates differently, so it **overrides** `rotate()`: it replaces the method it inherited with its own version.

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

With a shared `Shape` type, Team B could even write this, and every shape would do its own thing:

```java
Shape[] shapes = { square, circle, triangle, amoeba };
for (Shape s : shapes) {
    s.rotate();
    s.playSound();
}
```

Team A can't write that, no matter what they do. We'll get to inheritance later in the course.

## What Is an Object?

Team B's code is **object-oriented**. Each shape is an **object**:

- An object **knows** things. These are its **instance variables**: `width`, `height`, `xPoint`, `yPoint`
- An object **does** things. These are its **methods**: `rotate()`, `playSound()`

A **class** is the blueprint, and an **object** is the thing you make from it. There's one `Circle` class, but `new Circle()` can make as many circles as you want, each with its own width.

Team A's code is **procedural**: it's organized around **what the program does**. Object-oriented code is organized around **what the program is made of**. When the spec changes (and it always does), the object-oriented version has an obvious place to put the change.

> [!TIP]
> "But Team B's code is longer." That's true! The first version of anything is usually shorter to write procedurally. The fifth change is cheaper with objects. How many programs have you written that never changed?

## Review Quiz

[Shape Wars Quiz](quiz/review.csv)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 2: A Trip to Objectville
