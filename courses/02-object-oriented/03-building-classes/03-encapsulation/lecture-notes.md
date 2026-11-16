## The Problem

- Cat height = 0: "flat cat"
- ATM from last time: have them break it. withdraw(-200), balance = 1000000
- Ask: how do we stop this?

## Hiding the Data

- private vs public. They've typed public on every main since day one
- Make balance private and watch ATMDriver stop compiling
- No modifier = package access. That's why everything worked so far

## Rule of Thumb

- Private instance variables, public methods and constructors, getters/setters for what's needed

## Setters Can Say No

- setHeight > 9
- Fix deposit and withdraw together. My old version only checked amount < 0 on withdraw; also check amount <= balance (can't take out more than you have) and check deposit too
- Ask for other values that shouldn't be negative

## Read-Only

- I had setName commented out in the old ATM: that's the point. Name is set once by the constructor
- Balance only changes through deposit/withdraw

## Change Your Mind Later

- Circle radius: 100 programs set radius directly, now you want to block negatives
- With a setter you change one method

## Pillar One

- Back to the four pillars table, encapsulation is done
- From now on all their instance variables are private
