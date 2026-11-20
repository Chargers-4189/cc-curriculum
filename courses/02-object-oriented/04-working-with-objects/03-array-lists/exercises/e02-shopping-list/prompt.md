---
title: "Shopping List"
type: practice
difficulty: easy
---

You don't know how many items someone will type, so an array won't work. Use an `ArrayList<String>`:

1. Read items, one per line, until the user types `done` (don't add `done` to the list)
2. Print how many items there are, then each item numbered from 1

```
Enter items, then done:
zip ties
duct tape
bolts
done
You have 3 items:
1. zip ties
2. duct tape
3. bolts
```

(The tests type the items for you, so they won't show up in your output.)

**Hint:** read with `input.nextLine()` so items can have spaces in them.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get shopping-list
cd shopping-list
ccm test
```
