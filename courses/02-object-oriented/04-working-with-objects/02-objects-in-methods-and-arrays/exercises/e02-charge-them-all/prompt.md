---
title: "Charge Them All"
type: practice
difficulty: easy
---

`main` makes a team of three robots. Write two static methods below `main`:

- `public static void printTeam(Robot[] robots)` prints each robot on its own line as `<name>: <battery>%`
- `public static void chargeAll(Robot[] robots, int amount)` charges every robot by `amount` (use the robot's `charge` method)

```
Bolt: 40%
Volt: 90%
Amp: 10%
After charging:
Bolt: 65%
Volt: 100%
Amp: 35%
```

**Hint:** `chargeAll` doesn't return anything. Why do the robots in `main` still change?

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get charge-them-all
cd charge-them-all
ccm test
```
