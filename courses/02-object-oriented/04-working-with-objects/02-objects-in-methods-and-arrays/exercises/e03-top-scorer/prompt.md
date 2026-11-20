---
title: "Top Scorer"
type: practice
difficulty: easy
---

`main` has an array of players. Write two static methods below `main`:

- `public static Player topScorer(Player[] players)` gives back the **Player** with the most points. If there's a tie, give back the first one.
- `public static int totalPoints(Player[] players)` gives back everyone's points added up

```
Top scorer: Caleb with 27
Team total: 85
```

**Hint:** it's the "highest value" loop from the arrays lesson, but you keep track of the best **player**, not just the best number.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get top-scorer
cd top-scorer
ccm test
```
