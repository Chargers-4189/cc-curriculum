---
title: "Robot Drive"
type: homework
difficulty: medium
---

A `Robot` knows its `name`, its `battery` (0 to 100) and the `distance` it has driven so far. `main` is already written. Add these methods to `Robot`:

- `drive(int meters)`: driving uses **2% battery per meter**.
  - If the robot has enough battery, take the battery away, add the meters to `distance`, and print `<name> drove <meters> meters`
  - If it **doesn't** have enough battery, don't drive at all. Print `<name> doesn't have enough battery to drive <meters> meters`
- `charge(int amount)`: adds `amount` to the battery, but the battery can't go over 100
- `getBattery()`: gives back the battery
- `getDistance()`: gives back the distance

When it works, the program prints:

```
Bolt drove 10 meters
Bolt doesn't have enough battery to drive 20 meters
Bolt drove 15 meters
Battery: 0%
Distance: 25 meters
Battery: 80%
Bolt drove 15 meters
Distance: 40 meters
```

**Hints:**
- Work out the cost first: `int cost = meters * 2;`. Then compare it to `battery`.
- The robot starts at 50%. Trace it by hand: after `drive(10)` it has 30% left, which isn't enough for 20 meters.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get robot-drive
cd robot-drive
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
