---
title: "Unit Converter"
type: practice
difficulty: easy
---

Robot parts come in inches and pounds, but WPILib works in meters and kilograms. Write a `Convert` class that nobody needs to make an object of:

- Two **constants**: `METERS_PER_FOOT` is `0.3048` and `KILOGRAMS_PER_POUND` is `0.45359237`
- Three **static** methods that each take a `double` and give back a `double`:
  - `feetToMeters(feet)`
  - `metersToFeet(meters)`
  - `poundsToKilograms(pounds)`

`main` is already written:

```
10 feet is 3.05 meters
2 meters is 6.56 feet
120 pounds is 54.43 kilograms
One foot is 0.3048 meters
```

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get unit-converter
cd unit-converter
ccm test
```
