---
title: "Variables and Data Types"
---

# Variables and Data Types - Lecture Notes

## Variables

- Containers with a type, a name, and a value
- Open the follow-along: `String firstName;` then ask "declaration or initialization?"
- Then `firstName = "steve";` and print it
- `int myNum = 20;` does both at once

## Data Types

- Go through int, double, char, boolean with an example of each
- char uses single quotes, String uses double quotes; a common early mistake
- String isn't primitive; don't explain objects yet, "it's text, use it like the others"
- Answer the slide questions with the room:
  - Day of the month → int
  - double → prices, measurements, sensor readings; char → a letter grade, a key press
  - booleans → they're exactly what an if statement needs

## Casting

- Widening is automatic and safe (int → double)
- Narrowing must be written and loses information: `(int) 12.5` is 12, not 13
- Demo `(int) 19.99` → 19 so they see it truncates instead of rounding

## Naming

- camelCase for variables and methods, PascalCase for classes
- Bad names: `x`, `tP`, `thing`; better: `totalPrice`
- Comments are for the "why"; names should explain the "what"

## Scanner (brief)

- Show the Greeting example; just the pattern: import, create, `nextInt` / `nextDouble` / `nextLine`
- `print` vs `println` for prompts so the cursor stays on the same line
- We'll use this for the conditionals and loops programs
