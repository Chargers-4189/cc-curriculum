## Methods That Don't Need an Object

- Ask: when did we ever make a Math object? Never. Why not?
- round(42.2) is 42 no matter what, so there's no state to keep
- Try `new Math()` and read the error: the constructor is private

## Static Methods

- They've written static methods all of Fundamentals. Now they know what the word means
- Instance vs static table on the board
- Rule of thumb: if it doesn't use instance variables (and never will), it can be static
- Mention WPILib's Units class

## Static Can't Use Instance Variables

- Duck size in a static main: "whose size?"
- Why main always makes an object first

## Static Variables (spend time here)

- Try the instance variable counter first. Every robot says 1. Ask why
- Draw the memory map: one robotCount next to the class, name and battery in each robot
- Default values work the same for statics

## Constants

- static + final + public, ALL_CAPS
- Math.PI
- Constants.java in robot code. k prefix in WPILib

## final Variables

- final name set in the constructor. Compare to the read-only getter from Encapsulation
- final methods and classes come back with inheritance
