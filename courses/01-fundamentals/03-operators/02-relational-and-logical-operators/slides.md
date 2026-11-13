---
marp: true
paginate: true
---

<!-- Original deck: Week 2B - Java Fundamentals (August 21, 2026), slides 7-9 -->

## Relational Operators ⚖

- The common Relational Operators:
  - Equal → `==`
  - Not equal → `!=`
  - Greater than → `>`
  - Less than → `<`
  - Greater than or equal to → `>=`
  - Less than or equal to → `<=`
- Return booleans

**Be Cautious**
- `=` is used for assigning values
- `==` checks for equality

```java
myNum == 2
```

```java
i < 10
```

---

## Logical Operators 🔀

- The common Logical Operators:
  - And → `&&`
  - Or → `||`
  - Not → `!`
- Input: boolean
- Output: boolean

```java
x >= 0 && x < 10
```

```java
x > 0 || x == -2
```

---

## Operation Precedence

- Operators have **precedence**
  - Determines the order of evaluation
- Similar to PEMDAS
  - Parentheses → Exponents → Multiply/Divide → Add/Subtract
- Java uses this pattern
  - Parentheses → Unary (`!`, `-`) → Multiply/Divide → Add/Subtract → Relational (`>`, `<`, `>=`, `<=`) → Equality (`==`, `!=`) → `&&` → `||`

```
2 * 3 + 1     <- same as ->      (2 * 3) + 1 OR 6 + 1
```

```
2 * (3 + 1)     <- same as ->      2 * 4
```
