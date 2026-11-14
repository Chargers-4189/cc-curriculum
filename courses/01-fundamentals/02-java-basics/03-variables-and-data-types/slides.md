---
marp: true
paginate: true
---

<!-- Original deck: Week 1A - Introduction (August 10, 2026), slides 37-42 -->

# Java Basics

---

## 🫙 Variables

- Variables are just containers! They hold values
  - Declare with a data type: `String`
  - Assign with a name: `firstName`
  - Initialize with a value: `"Steve"`
- Variables are used in **various ways**
  - Calculations, storing information, controlling program flow, and more
- They are used in nearly every program to **store and manipulate** data

```java
String firstName;
firstName = "steve";
```

---

## Data Types 🗃

- Primitive data types are the simplest data types
  - `int` ► Represents whole numbers -/+
  - `double` ► Represents decimal numbers
  - `char` ► Represents a single character
  - `boolean` ► Represents a true or false value
- Range & Precision:
  - Int can store **-2 to +2 billion**
  - Double can store decimals at **high precision**
- A variable's type can't change; to store something different, **assign a new value**.

**Think about it:**
- What primitive data type would you use for the date of the month?
- What exactly could double be used for? What about char?
- Booleans are very useful for conditional statements, why is that?

---

## Data Types 2 🗃

Converting a value to another data type: **Type Casting**

- Two types of Type Casting
  - **Widening** (automatic)
    - byte -> short -> int -> long -> float -> double
  - **Narrowing** (reverse)
- When narrow casting, you must do it **manually** by adding the **type you're converting to in front of the value** in ()

```java
int myNum = 12;
double myNewDouble = myNum;
System.out.println(myNewDouble); // Outputs 12.0 - widening

double myDouble = 12.5;
int myNewNum = (int) myDouble;
System.out.println(myNewNum);    // Outputs 12 (NO ROUNDING) - narrowing
```

*Note: Consider size & memory when choosing data types. Int is more efficient than double due to decimal precision*

---

## 🗣 Declaration & Initialization

- Declaration
  - **Specifies the Data Type and Name**
  - `dataType variableName;`
- Initialization
  - **Assign a value** to your variable.
  - `variableName = value;`
  - '=' assigns the value to your variable.
- Use meaningful variable names to improve **code readability** and **avoid errors**.

```java
int age;
double price = 19.99;
char grade = 'A';
boolean isJavaFun = false;
```

---

## Naming Convention ✍

- Use **Descriptive Variable Names**
  - tP -> totalPrice
- Follow **camelCase**
  - Capitalize the first letter of every word except the first.
- Keep names clear and **concise**.
- Stick to a **consistent naming** style throughout your code.

- **Class Names**
  - Use noun/noun phrases
  - Camel case, but with capital first letter.
- **Method Names**
  - Use verbs/verb phrases.
  - Follow camel case.
- Use **comments sparingly**
  - Use good names so your code is self explanatory.
