---
title: "Thermostat"
type: practice
difficulty: medium
---

A thermostat can only be set from **60 to 80** degrees. Write the `Thermostat` class so nobody can get it outside that range:

- A **private** `int temperature`
- A constructor that takes the starting temperature
- `getTemperature()`
- `setTemperature(int temperature)`: anything below 60 becomes 60, and anything above 80 becomes 80
- `up()` and `down()`: change the temperature by 1, but still stay from 60 to 80

`main` is already written:

```
72
80
78
60
61
```

**Hint:** the constructor, `up()` and `down()` can all call `setTemperature`. Then the 60 to 80 check is only written once.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get thermostat
cd thermostat
ccm test
```
