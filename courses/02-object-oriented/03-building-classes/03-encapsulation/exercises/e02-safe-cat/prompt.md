---
title: "Safe Cat"
type: practice
difficulty: easy
---

Right now anyone can do `tom.height = 0;` and flatten the cat. Encapsulate it:

1. Make `height` **private**
2. Add a public `getHeight()` that gives back the height
3. Add a public `setHeight(int height)` that only changes the height if the new height is **more than 9**. Otherwise it leaves the height alone.

`main` is already written:

```
Height: 27
Height: 27
Height: 12
```

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get safe-cat
cd safe-cat
ccm test
```
