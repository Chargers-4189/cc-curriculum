> **Objectives**
> - Explain how an object's state affects its behavior
> - Write methods that take parameters and return values
> - Write getters and setters
> - Call methods on an object (and know why you can't call them on the class)
>
> **Prerequisites**
> - [Object Variables](../../02-classes-and-objects/02-object-variables/lecture.md)
> - [Writing Methods](../../../01-fundamentals/07-methods/01-writing-methods/lecture.md)

*Parts of this lesson are adapted from Head First Java (Sierra, Bates & Gee), Chapter 4.*

## Follow Along

Write `Dog.java`, `Fish.java` and `BehaviorTester.java` along with this lesson. Get the starter files in Charging Courses Labs with `ccm get behavior-demo`. The class code goes in `Dog.java` or `Fish.java`, and the code that uses it goes in `BehaviorTester.java`, each under its matching `// --- Section ---` comment.

## State and Behavior

Objects have **state** and **behavior**: what an object **knows** and what it **does**. State is its instance variables (with whatever values they have right now). Behavior is its methods. Calling a method on an object is asking that object to do something.

A class describes both:

| Song | |
|---|---|
| **Instance variables** (state, knows) | `title`, `artist` |
| **Methods** (behavior, does) | `setTitle()`, `setArtist()`, `play()` |

Can every object of a class have different methods? No. Every `Song` has the **same** `play()` method. But the method can **behave** differently depending on the object's instance variables. Calling `play()` on one song plays "Sing" by Travis, and calling it on another plays "My Way". The method code is the same. The values are different.

## State Affects Behavior

Each object has its own values. Dog A can be named "Fido" and weigh 70 pounds, and Dog B can be "Mochi" and weigh 10. A small dog's bark is different from a big dog's bark, so `bark()` can use `size` to decide what to print:

```java
public class Dog {
    int size;
    String name;

    void bark() {
        if (size > 60) {
            System.out.println("Wooof! Wooof!");
        } else if (size > 14) {
            System.out.println("Ruff! Ruff!");
        } else {
            System.out.println("Yip! Yip!");
        }
    }
}
```

```java
Dog one = new Dog();
one.size = 70;
Dog two = new Dog();
two.size = 8;
Dog three = new Dog();
three.size = 35;

one.bark();    // Wooof! Wooof!
two.bark();    // Yip! Yip!
three.bark();  // Ruff! Ruff!
```

Same method, three different barks. That's an object's behavior acting on its state.

## Sending Things to a Method

This should look familiar from Fundamentals. Methods can take inputs:

- A caller **passes arguments**
- A method **takes parameters**

A parameter is just a local variable that gets its starting value from the caller. **If a method takes a parameter, you have to pass it something**, and it has to be the right type.

```java
public class Fish {
    int weight;
    String diet;   // "herbivore" or "carnivore"

    void eat(int numOfBites) {
        while (numOfBites > 0) {
            if (diet.equals("herbivore")) {
                System.out.println("Eating plants...");
            } else if (diet.equals("carnivore")) {
                System.out.println("Eating other fish...");
            } else {
                System.out.println("Don't know my diet.");
            }
            numOfBites--;
        }
    }
}
```

```java
Fish myFish = new Fish();
myFish.diet = "herbivore";
myFish.eat(3);   // 3 is the argument, it lands in numOfBites
```

`eat` uses both: the parameter (`numOfBites`, from the caller) and the instance variable (`diet`, from the fish).

> [!WARNING]
> Compare `String`s with `.equals`, not `==`. `==` checks if two references point to the **same object**, which isn't the same as having the same letters.

## Getting Things Back

Every method has a return type. So far most of ours have been `void`, which means they don't give anything back. If you say a method returns something, **you have to return a value of that type**:

```java
int getWeight() {
    return weight;
}
```

```java
int w = myFish.getWeight();
System.out.println("My fish weighs " + w);
```

Anywhere you could use an `int`, you can use a method call that returns an `int`. So instead of `int x = 3 + 24;` you could write `int x = 3 + myFish.getWeight();`.

You don't **have** to use a return value. Java is fine with `myFish.getWeight();` on its own line, it just throws the value away.

## More Than One Parameter

Separate parameters with commas. When you call the method, the arguments land in the parameters **in order**, so they have to match the type and order:

```java
void swim(int distance, int speed) {
    System.out.println("Swimming " + distance + " meters at speed " + speed);
}
```

```java
myFish.swim(20, 3);   // distance is 20, speed is 3
```

You can pass variables too, as long as their types match: `myFish.swim(laps, fast);`.

## Passing a Copy

Remember [pass-by-value](../../../01-fundamentals/07-methods/01-writing-methods/lecture.md#pass-by-value)? It works the same way for methods in a class. When you call `myFish.eat(bites)`, the value in `bites` gets **copied** into `numOfBites`. The method counts `numOfBites` down to 0, but `bites` back in `main` doesn't change.

## Getters and Setters

Now let's put parameters and return types to good use. A **getter** gives back the value of an instance variable. A **setter** takes an argument and uses it to set an instance variable.

```java
String getName() {
    return name;
}

void setName(String newName) {
    name = newName;
}

int getSize() {
    return size;
}

void setSize(int newSize) {
    size = newSize;
}
```

The names follow a pattern: `get` or `set` plus the variable's name, in camelCase. For a `boolean`, the getter usually starts with `is` instead: `isOn()`, `isHungry()`.

Right now these don't seem to do much, since we could just use `one.name` directly. In the encapsulation lesson you'll see why getters and setters matter.

## Instance Methods Need an Object

`bark()`, `eat()` and `getName()` don't have `static`, so they're **instance methods**: they run on a specific object, using that object's instance variables. The object you call the method on is the **calling object**.

```java
one.bark();   // the calling object is one, so it uses one's size
Dog.bark();   // won't compile: which dog?
```

That's different from `Math.abs(-5)` or the methods you wrote in Fundamentals. Those are `static`, so they belong to the class and you call them with the class name.

## Review Quiz

[Object Behavior Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Light Switch

[Light Switch](exercises/e02-light-switch/prompt.md)

### 2. Gas Tank

[Gas Tank](exercises/e03-gas-tank/prompt.md)

## Homework

### Robot Drive

[Robot Drive](exercises/e04-robot-drive/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 4: How Objects Behave
- Introduction to Java Programming (Liang), 9.5.1: Accessing an Object's Data and Methods
