> **Objectives**
> - Compare values with relational operators and get a `boolean` result
> - Avoid the `=` vs `==` mistake
> - Compare decimals and Strings correctly
> - Combine conditions with `&&`, `||`, and `!`
> - Use short-circuit evaluation to prevent errors
> - Know the order Java evaluates operators in
>
> **Prerequisites:** [Arithmetic Operators](../01-arithmetic-operators/lecture.md)

## Follow Along

Get the starter file in Charging Courses Labs with `ccm get relation-demo` and open `Relation.java`. Write each section's code under its `// --- Section ---` comment and run it. If a name is already used, pick a new one.

## Relational Operators

Relational operators **compare** two values and **return a boolean**: `true` or `false`.

| Operator | Meaning | `a = 10, b = 20` |
|---|---|---|
| `==` | Equal | `a == b` → `false` |
| `!=` | Not equal | `a != b` → `true` |
| `>` | Greater than | `a > b` → `false` |
| `<` | Less than | `a < b` → `true` |
| `>=` | Greater than or equal to | `a >= b` → `false` |
| `<=` | Less than or equal to | `a <= b` → `true` |

```java
int a = 10;
int b = 20;
System.out.println("a < b: " + (a < b));   // a < b: true
System.out.println("a == b: " + (a == b)); // a == b: false
```

Put parentheses around `(a < b)`. Without them, Java joins `"a < b: " + a` as text first.

### Be Cautious: `=` vs `==`

- `=` is for **assigning** values
- `==` is for **comparing** values

`x = 5` puts 5 into `x`. `x == 5` asks "is `x` equal to 5?"

> [!WARNING]
> **Try it:** add `System.out.println("a == b: " + (a = b));` with only **one** `=`. It prints `20`, because `=` puts 20 into `a`. Comment it out.

## Comparing Different Types

When you compare an `int` and a `double`, the `int` is converted to a `double` first:

```java
System.out.println(10 == 10.0); // true - 10 becomes 10.0
```

## Comparing Decimals

Computers can't store most decimals exactly:

```java
System.out.println(0.1 + 0.2);         // 0.30000000000000004
System.out.println((0.1 + 0.2) == 0.3); // false!
```

Don't use `==` on doubles. Check if the difference is **close enough to 0**:

```java
double c = 0.1 + 0.2;
double d = 0.3;
double THRESHOLD = 1e-9; // 0.000000001
System.out.println(Math.abs(c - d) < THRESHOLD); // true
```

`Math.abs` gives the absolute value.

## Comparing Strings

To check if two Strings have the same text, use **`.equals()`**:

```java
String answer = "yes";
System.out.println(answer.equals("yes")); // true
```

`==` on Strings can say `false` even when the text matches. We'll cover why in the Object Oriented course.

## Logical Operators

Logical operators **combine booleans** into one boolean.

| Operator | Name | True when... |
|---|---|---|
| `&&` | AND | **both** sides are true |
| `\|\|` | OR | **at least one** side is true |
| `!` | NOT | flips the value: `!true` is `false` |

```java
int x = 10;
System.out.println(x > 0 && x < 50); // true  - x is between 0 and 50
System.out.println(x > 0 || x < 5);  // true  - the left side is true
System.out.println(!true);           // false
```

```java
x >= 0 && x < 10    // is x between 0 and 9?
x > 0 || x == -2    // is x positive, or exactly -2?
```

## Short-Circuit Evaluation

`&&` and `||` **skip the right side** if the left side already decides the answer.

- `&&`: if the left side is `false`, the whole thing is `false`, so the right is never checked
- `||`: if the left side is `true`, the whole thing is `true`, so the right is never checked

This can guard against errors:

```java
int u = 10, r = 15;
System.out.println(u < r || 0 == 1 / 0); // true - the divide by zero never runs
System.out.println(u > r && 0 == 1 / 0); // false - same here
```

## Operator Precedence

Operators have **precedence**, which determines the order of evaluation. It's similar to PEMDAS, from first to last:

1. Parentheses `( )`
2. Unary operators: `!`, `-` (negative), `++`, `--`
3. Multiply, divide, modulus: `* / %`
4. Add, subtract: `+ -`
5. Relational: `< > <= >=`
6. Equality: `== !=`
7. Logical AND `&&`
8. Logical OR `||`

Operators on the same level go left to right.

```java
2 * 3 + 1          // same as (2 * 3) + 1, which is 7
2 * (3 + 1)        // same as 2 * 4, which is 8
x > 0 && x < 10    // the comparisons happen first, then &&
```

## Further

Not required:

- **XOR `^`** is true only when the two sides are **different**: `true ^ false` is `true`, `true ^ true` is `false`.
- **Non-short-circuit `&` and `|`** always evaluate both sides. You'll rarely need these.

> [!WARNING]
> **Try it:** change `||` to `|` in your short-circuit line and run it. It crashes, because `|` runs the `1 / 0`. Comment it out.

## Review Quiz

[Relational and Logical Operators Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes.

### 1. Is It Even?

[Is It Even?](exercises/e02-is-it-even/prompt.md)

### 2. Divisible by 5 and 6

[Divisible by 5 and 6](exercises/e03-divisible-by-5-and-6/prompt.md)

### 3. Same Word

[Same Word](exercises/e04-same-word/prompt.md)
