---
title: "Arrays"
---

# Arrays - Lecture Notes

Keep this one surface level: what arrays are and how to use them. Save objects/references for Object Oriented.

## Why Arrays

- 30 test scores → 30 variables is unmanageable
- One name, many values of the same type, fixed size

## Creating

- Initializer list `{...}` when you know the values
- `new int[7]` when you only know the size; default values (0, false)

## Indexes

- Start at 0; draw the boxes with indexes on the board
- Read and change elements: `scores[0]`, `scores[2] = 75`
- `.length`; last index is `length - 1`

## Out of Bounds

- `scores[5]` on a 5-element array; read the exception together

## Loops

- `for (int i = 0; i < arr.length; i++)` is the pattern to memorize
- Sum/average (cast to double; callback to integer division)
- Max: start with the first element, compare the rest

## Arrays Are Objects

- Mention it because it's on the slide; "that's why `new` and `.length`"
- Don't go further; it comes back in Object Oriented
