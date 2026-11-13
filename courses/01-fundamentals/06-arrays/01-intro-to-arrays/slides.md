---
marp: true
paginate: true
---

<!-- Original deck: Week 2B - Java Fundamentals (August 21, 2026), slide 14 -->

## Arrays 📃

Arrays are just a tray of containers, they allow you to use an index position to get to any element in the array

- Every element in an array is just a variable
  - include both **Primitive** and **Object Reference** variables
- *ARRAYS are always objects, whether they're declared as a primitive or object reference array, an array is an object*

```java
int[] scores = {90, 85, 72, 100, 64};
System.out.println(scores[0]);      // 90
System.out.println(scores.length);  // 5
```

<!-- The original slide was live-coded from an empty Main.java; the snippet above is a placeholder example. -->
