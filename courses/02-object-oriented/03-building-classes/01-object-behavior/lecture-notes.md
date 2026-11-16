## State and Behavior

- Review: state = instance variables with their current values, behavior = methods
- Song table on the board. Ask: can every object of a class have different methods? Sort of: same methods, different values

## State Affects Behavior

- Dog barks. Make three dogs, predict each bark before running
- "Methods use instance variables" is the whole point of this lesson

## Sending Things to a Method

- This is mostly review from Fundamentals methods
- Caller passes arguments, method takes parameters. Parameters are local only
- Fish `eat(numOfBites)`: uses a parameter and an instance variable together
- My old notes had `diet == "herbivore"`. Show why `.equals` is the right one (ties back to references)
- Method signature on the board: [return type] [name]([type name, ...]) { body }

## Getting Things Back

- `getWeight()`. You can use a method call anywhere a value of that type fits
- Ignoring a return value is allowed

## More Than One Parameter

- Order and type have to match. Try `swim(20)` and read the error

## Getters and Setters

- Just the pattern today. They'll ask "why not just use `dog.name`?" Good question, that's the encapsulation lesson

## Instance Methods

- `Dog.bark()` won't compile. Compare with `Math.abs`, which is static
