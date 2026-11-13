---
marp: true
paginate: true
---

<!-- Original deck: Week 2B - Java Fundamentals (August 21, 2026), slide 12 -->

## While Loops 🔁

- Loops run by running a **conditional test**
  - **While loops** run everything in its loop block as long as the condition is true
- The loop block is defined by curly brackets `{}`

```java
class Main {
    public static void main(String[] args) {
        System.out.println("Before Loop");
        int i = 1;
        while (i < 20) {
            System.out.println("Loop: " + i);
            i++;
        }
        System.out.println("After Loop");
    }
}
```

<!-- Output: Before Loop, Loop: 1 ... Loop: 19, After Loop -->
<!-- The original slide was live-coded from an empty Main.java; this is the code that produces its output. -->


