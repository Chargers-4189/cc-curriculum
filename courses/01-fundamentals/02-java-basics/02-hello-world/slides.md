---
marp: true
paginate: true
---

<!-- Original deck: Week 1A - Introduction (August 10, 2026), slides 34-36 -->

# Creating Your First Program

---

## Hello World 👋

- Let's create a simple Hello World Program
  - **Class declaration:** `HelloWorld {...}`
  - **Main Method:** `public static void main()`
  - **Print to Console:** `System.out.println()`
- **Class Declaration:**
  - We're creating a class called HelloWorld.
- **Main Method:**
  - Using the Main Method to start
- **Print to Console:**
  - `System.out.println()` prints a line of output

```java
// HelloWorld.java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

---

## Hello World 2 👋

- Notice how our filename and class is the same
  - This keeps your code **organized** and makes your classes **easier** to find and understand.
  - This is a **strict rule** for public classes: the file must be named after the class.
- `System.out.println` is a function that is a form of output in Java
- You can see the **main method** is our only method and all our code is within it.

**Think about it:**
- Why would it be important for your code to be readable?
- What do you think could be another output form?
- What is the purpose of Main? Why is it necessary for any Java program?
- Every statement in Java must end with what?
