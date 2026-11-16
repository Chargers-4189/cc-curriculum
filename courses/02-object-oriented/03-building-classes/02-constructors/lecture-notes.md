## Methods Review

- State = instance variables with current values. Behavior = methods; calling one asks the object to do something
- Circle: setRadius, getRadius, calculateArea
- End on `new Circle()`: are we calling a method called Circle? Let them guess

## Making an Object

- The three steps on the board: declare, create, link
- Constructor rules: same name as the class, no return type (not even void), only runs with `new`

## Where Did the Constructor Come From?

- The compiler writes `public Circle() {}` if you don't write any

## Writing a Constructor

- Duck prints Quack. Run it, then set size and name in the constructor
- Show the inside-the-constructor diagram: main has no myDuck yet. The constructor runs before the reference gets the object

## Why Not a Setter?

- Duck without a size for one line. How would the user know to call setSize?

## Overloaded Constructors

- Duck(), Duck(int), Duck(int, String), from Nature.java
- Different parameter lists. Names don't count, types and order do
- Ask: can I have Duck(int size) and Duck(int weight)? No

## The Compiler Backs Off

- Comment out the no-arg constructor, `new Duck()` breaks
- `public void Duck()` is a method. Shows up on tests a lot

## this

- `size = size;` does nothing. Run it to prove it
- `this.size` = the calling object's size
- Hidden variables: the parameter hides the instance variable
