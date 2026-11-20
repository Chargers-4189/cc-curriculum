---
title: "Remove the Negatives"
type: practice
difficulty: medium
---

Fill in `removeNegatives`, which removes every number less than 0 from the list. It doesn't return anything: it changes the list `main` passed in.

```
Before: [4, -2, -7, 5, -1, 8]
After: [4, 5, 8]
```

Try the obvious way first: loop from 0 up to `size()` and remove the negatives. Run it. Is `-7` still there? Draw what happens to the indexes when you remove `-2`.

**Hint:** when you remove something, everything after it shifts down one spot. Looping **backward** (from `size() - 1` down to 0) fixes it, since the items you haven't looked at yet never move.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get remove-the-negatives
cd remove-the-negatives
ccm test
```
