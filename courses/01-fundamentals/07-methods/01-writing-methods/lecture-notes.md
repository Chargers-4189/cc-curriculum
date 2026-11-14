## Why

- Start with the two copy-pasted loops (commented out in the follow-along)
- Ask: what's different? Only two numbers
- Write `sumOfRange` once and call it with several ranges
- They've used methods since day one: println, Math.random, Math.abs

## Anatomy

- Label the header on the board: modifiers, return type, name, parameters
- The four questions: name, needs, gives back, how
- Parameters vs arguments
- `return` jumps back immediately; nothing after it runs
- Every parameter needs its own type: `max(int a, b)` won't compile

## void vs Returning

- printGrade vs getGrade; ask "which is better?"
- Returning is more flexible: print it, store it, compare it
- Every path must return; the compiler is strict
- yes/no methods: boolean, named like questions (isPrime, isLeapYear)

## Pass-by-Value (spend real time here)

- Predict-then-run with `increment(x)` and `swap(num1, num2)`
- Most will expect swap to work; run it and let it sink in
- Draw two separate boxes with a one-way arrow
- Renaming the parameter to `num1` changes nothing: same name, different box
- How do you "fix" swap? You don't; you return values instead

## Scope

- A variable lives until the closing brace of its block
- Loop header variables die with the loop
- Parameters are local variables; that's why swap fails

## Optional

- Overloading: `max` for ints, doubles, three doubles
- Stepwise refinement + stubs; tell them this is how to do the credit card homework

## Homework: Credit Card Validator

- Give them the method headers; they fill in the bodies
- Stub everything first so it compiles
- Order: getDigit → getSize → getPrefix → prefixMatched → the two sums → isValid → main
- `ccm test` tests each method separately, so they can see progress
- Use `long` for card numbers; literals need `L`
