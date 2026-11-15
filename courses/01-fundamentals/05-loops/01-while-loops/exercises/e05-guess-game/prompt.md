---
title: "Guess the Number"
type: homework
difficulty: medium
---

The computer picks a random number from 0 to 100. The user keeps guessing until they get it, and after each guess the program says if it was too high or too low.

```
Enter your guess:
50
Try again, too high
Enter your guess:
25
Try again, too low
Enter your guess:
37
You win!
```

Build it with the 3-step recipe from the lesson:

1. Write the code to read **one** guess and compare it. Run it.
2. Wrap it in `while (true) { ... }`.
3. Replace `true` with a real condition so the loop stops when the guess is right.

**Hint:** what should `guess` start as before the loop? Why not `0`?

**Challenge:** limit the player to 7 attempts, and tell them how many guesses they used.

## In Labs

Download it and write your code in `Main.java`:

```bash
ccm get guess-game
cd guess-game
```

There are no automatic tests because the numbers are random. Run it a few times, then paste all of `Main.java` into the assignment.
