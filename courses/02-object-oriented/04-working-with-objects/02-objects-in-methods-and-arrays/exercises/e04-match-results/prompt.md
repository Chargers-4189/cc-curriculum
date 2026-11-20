---
title: "Match Results"
type: homework
difficulty: medium
---

A competition schedule has six matches, but only four have been played. The ones that haven't been played are `null` in the array. The `Match` class is already written. Each match knows its number, the red alliance's score and the blue alliance's score.

Write three static methods below `main`. Each one has to **skip the `null` slots**:

- `public static int countPlayed(Match[] matches)`: how many matches have been played (aren't `null`)
- `public static int redWins(Match[] matches)`: how many matches red won (red's score is higher than blue's)
- `public static Match highestScoring(Match[] matches)`: the match with the most total points (red + blue). If there's a tie, give back the first one.

When it works, the program prints:

```
Played: 4
Red won: 2
Highest scoring: match 3
Red won: 3
```

Notice the last line. `main` added a penalty to match 4 through the array, and your `redWins` sees it, because the array holds references to the same match objects.

**Hints:**
- Calling a method on a `null` slot crashes with a NullPointerException. Check `matches[i] != null` first.
- For `highestScoring`, you can't start with `matches[0]` like usual, since the first slot could be `null`. Start with `Match best = null;` and take the first match you find.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get match-results
cd match-results
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
