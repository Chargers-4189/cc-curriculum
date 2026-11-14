## Relational Operators

- Follow-along: `a = 10, b = 20`; print all six comparisons, predict each first
- They always produce a boolean; tie back to the boolean data type
- Why the parentheses in `"a < b: " + (a < b)`

## = vs ==

- Assign vs compare; uncomment the `(a = b)` line to show the compile error
- Very common first-week bug

## Mixed Types and Decimals

- `10 == 10.0` is true: the int is promoted
- `0.1 + 0.2` → 0.30000000000000004; computers store decimals in binary (like 1/3 in decimal)
- Compare with a threshold: "close enough to zero" means equal; use `Math.abs`

## Strings

- `.equals()` for text; `==` can be false even when the text matches
- Don't explain references yet; "we'll see why in Object Oriented"

## Logical Operators

- AND: both; OR: at least one; NOT: flip
- Real examples: "between 0 and 10", "is it the weekend: Saturday OR Sunday"
- Short-circuit: show `u < r || 0 == 1/0` doesn't crash
- Practical use: `str != null && str.length() > 0`, `divisor != 0 && ...`

## Precedence

- Correct the PEMDAS myth: multiply/divide are one level, add/subtract are one level
- Arithmetic before comparisons before `&&` before `||`
- When in doubt, parentheses

## Your Turn

- `age` between 16 and 21: `age > 16 && age < 21`
- Optional: XOR `^` (true when they differ)
