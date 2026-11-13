---
title: "Switch Statements"
---

# Switch Statements - Lecture Notes

## Setup

- Tax filing status example; write the if ladder first so they feel the repetition
- Same variable compared over and over → switch

## Syntax

- `switch (value)`, `case X:`, `break;`, `default:`
- default is the final else
- Works with int, char, String; not double or boolean

## Fall-Through

- Remove the breaks live and run it: everything after the match prints
- Intentional fall-through for shared cases (weekend example)

## Choosing

- switch: one value, exact matches
- if: ranges and compound conditions

## Optional

- Arrow form `case 0 ->` (Java 14+), no break needed

## Homework: Day of the Week

- Walk through Zeller's formula variables; emphasize integer division
- January/February are months 13/14 of the previous year; most common mistake
- The switch turns h into a day name (0 = Saturday)
- They can check their own answer against a calendar, and with `ccm test`
