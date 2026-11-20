## Passing an Object to a Method (spend time here)

- Predict-then-run with chargeUp. Most will expect amount to change too, or bolt not to
- Draw two frames on the board: chargeUp and main, two amounts, one robot
- Java is still pass-by-value. The value in bolt just happens to be a reference
- Liang calls this pass-by-sharing: the method and the caller share the object

## Changing the Object vs Changing the Variable

- replace(bolt): predict first. Draw r's arrow moving, bolt's arrow staying put
- Tie back to swap from Fundamentals Methods

## Returning an Object

- makeSpare: r goes away, the robot doesn't. Something still refers to it

## Arrays Are Objects

- Payoff of "we'll dig into this in OOP" from the arrays lesson
- Passing an int[] to a method that changes it: the caller sees it

## Arrays of Objects

- new Robot[3] makes zero robots. Ask how many objects there are (1: the array)
- Draw the array with null slots, then fill two
- Try team[2].getName() for the crash
- Two levels: team -> array, team[1] -> robot

## Looping Over Objects

- Average battery with a regular loop, then point out i is only used for team[i]. Rewrite it as a for-each
- Say it out loud: "for each Robot r in team"
- Rule: for-each unless you need the index. Ask for examples that need the index (slot numbers, replacing a slot, starting at 1)
- r is a copy of the reference, same as a parameter: r.charge works, r = new Robot(...) doesn't change the array. Ties back to Changing the Object vs Changing the Variable
- lowest(...) starts at index 1, so it keeps the regular loop and returns the robot itself
- Null checks for arrays with empty slots (the homework needs this)
