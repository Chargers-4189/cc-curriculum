## Where We Left Off

- Quick recap of Shape Wars: procedural vs object-oriented, the Shape diagram
- Words they heard: class, method, instance variable (attribute), inheritance, override

## The Four Pillars

- Just the names for now: encapsulation, inheritance, polymorphism, abstraction
- We'll touch on encapsulation and abstraction a bit today

## Classes and Objects

- Board: classes are blueprints to create objects
- A class is not an object. House blueprint vs houses
- Quick review of the basic data types (int, double, boolean, String, char) since instance variables use them

## Knows / Does

- Board: what the object knows → instance variables, what it does → methods
- Have them call out knows/does for a 2008 Honda Odyssey, a shopping cart, an alarm, a button
- Button: show one class with different values ("Backspace" pink, "Nuclear launch" red, "A" green)

## Cat Follow Along

- Write `Cat.java` together. No values on the instance variables: we don't know which cat yet
- No `static` on the methods. They belong to each cat
- `CatTester.java`: `Cat myCat;` holds nothing yet (null, more on that next lesson), then `new Cat()`
- Dot operator: call methods and set instance variables
- Try `Cat.meow();` and read the error
- Second cat: same method, different name

## Homework

- Movie class. `main` is given, they only write the class (three instance variables and `playIt`)
- Last time this was hard when they also had to write the tester, so the tester is done for them now
