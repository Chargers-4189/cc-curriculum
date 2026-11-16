> **Objectives**
> - Explain why exposed instance variables are a problem
> - Use `private` and `public` to control what other classes can touch
> - Write setters that check their input before changing an object
> - Make a value read-only
> - Explain encapsulation, the first pillar of OOP
>
> **Prerequisites:** [Constructors](../02-constructors/lecture.md)

*Parts of this lesson are adapted from Head First Java (Sierra, Bates & Gee), Chapter 4, and Introduction to Java Programming (Liang), Chapter 9.*

## Follow Along

Write `ATM.java` and `ATMDriver.java` along with this lesson. Get the starter files in Charging Courses Labs with `ccm get atm-demo`. Write each section's code under its matching `// --- Section ---` comment, and run `ATMDriver` as you go.

## The Problem

Up to now, we've been leaving our data out where anyone can see it, and even change it. Any code with a reference to an object can reach its instance variables with the dot operator:

```java
theCat.height = 27;
```

That's fine, until someone does this:

```java
theCat.height = 0;
```

A cat with a height of 0. Nothing stopped it.

Here's a worse one. This `ATM` keeps track of someone's money:

```java
public class ATM {
    int balance;
    String name;

    public ATM(String newName, int newBalance) {
        name = newName;
        balance = newBalance;
    }

    int deposit(int amount) {
        balance = balance + amount;
        return balance;
    }

    int withdraw(int amount) {
        balance = balance - amount;
        return balance;
    }
}
```

```java
ATM quinnAccount = new ATM("Quinn", 0);
quinnAccount.withdraw(-200);        // a negative withdraw adds $200
quinnAccount.balance = 1000000;     // or skip that and set the balance
```

A reference is like a remote control, and in the wrong hands it's dangerous. We need a way to **force** other code to go through methods, so the methods can check what's happening first.

## Hiding the Data

You do that with **access modifiers**. You already know one: `public`, from every `main` method.

- **`public`**: any class can use it
- **`private`**: only code **inside this class** can use it

Mark the instance variables `private`:

```java
public class ATM {
    private int balance;
    private String name;
    ...
}
```

Now `quinnAccount.balance = 1000000;` in `ATMDriver` **won't compile**. The only way to change the balance is through `ATM`'s own methods.

> [!WARNING]
> **Try it:** make `balance` and `name` private, then try setting `quinnAccount.balance` in `ATMDriver`. Read the error, then comment it out.

If you leave the modifier off (like we have been), anything in the same **package** (the same folder, for us) can use it. That's why everything worked until now.

| Modifier | Who can use it |
|---|---|
| `public` | Any class |
| (none) | Classes in the same package |
| `private` | Only the class it's in |

`private` only goes on things that belong to a class: instance variables, methods and constructors. Putting it on a local variable is a compile error.

## The Rule of Thumb

For now, here's the rule:

- Make your **instance variables `private`**
- Make your **constructors and methods `public`** (unless a method is only a helper for the class itself)
- Give other classes **getters and setters** for the values they need

When you know more Java, you'll bend this sometimes. But it'll keep you safe for now. This is **encapsulation**: keeping an object's data inside it, and controlling how the outside world gets to it.

## Setters Can Say No

Here's why getters and setters matter. Since everyone has to go through the setter, **the setter can check the value** before using it:

```java
public void setHeight(int height) {
    if (height > 9) {
        this.height = height;
    }
}
```

Now no cat can be shorter than 10. A setter can ignore a bad value (like this one), change it to the closest good value, or show an error. It's your call.

Same with the ATM. `deposit` and `withdraw` are how the balance changes, so they're where we check:

```java
public int deposit(int amount) {
    if (amount > 0) {
        balance = balance + amount;
    }
    return balance;
}

public int withdraw(int amount) {
    if (amount > 0 && amount <= balance) {
        balance = balance - amount;
    }
    return balance;
}
```

```java
quinnAccount.deposit(10);
quinnAccount.withdraw(-100);   // ignored
quinnAccount.withdraw(50);     // ignored, there's only $10
System.out.println(quinnAccount.getBalance());   // 10
```

Think of all the things that would break with a negative number: an ATM balance, a cat's height, a robot's battery, the number of bathrooms in a house. Most values have limits, and encapsulation is how you protect them.

## Read-Only

Sometimes a value shouldn't change at all after the object is made. Just give it a getter and **no setter**:

```java
public String getName() {
    return name;
}

public int getBalance() {
    return balance;
}
```

Other classes can see the name and balance, but there's no `setName` or `setBalance`. The name is set once by the constructor, and the balance only changes through `deposit` and `withdraw`.

## You Can Change Your Mind Later

"But some setters don't check anything. Why not just make that variable public?"

Because with a setter, **you can change your mind later without breaking anyone's code.** Say a hundred other programs use your `Circle` class, and they all set `c.radius = ...` directly. One day you realize a radius should never be negative. To fix it, you'd have to change your class **and** all hundred programs.

If they'd all been calling `setRadius`, you'd only change `setRadius`:

```java
public void setRadius(double radius) {
    if (radius >= 0) {
        this.radius = radius;
    } else {
        this.radius = 0;
    }
}
```

Nobody else has to change a thing. That's the other half of encapsulation: the **inside** of a class can change, as long as its public methods still work the same.

## Pillar One: Encapsulation

That's the first of the four pillars:

| Pillar | |
|---|---|
| **Encapsulation** | An object keeps its data private and controls how it changes, through its methods |
| Inheritance | Coming up |
| Polymorphism | Coming up |
| Abstraction | Coming up |

From now on, every class you write should have private instance variables.

## Review Quiz

[Encapsulation Quiz](quiz/review.csv)

## Practice

Write your code in each editor and click **Test Run** until every test passes. (Or `ccm get` it and work in Labs.)

### 1. Safe Cat

[Safe Cat](exercises/e02-safe-cat/prompt.md)

### 2. Thermostat

[Thermostat](exercises/e03-thermostat/prompt.md)

## Homework

### Fan Class

[Fan Class](exercises/e04-fan-class/prompt.md)

## Readings

### Further

- Head First Java (Sierra, Bates & Gee), Chapter 4: Encapsulation
- Introduction to Java Programming (Liang), 9.8: Visibility Modifiers
- Introduction to Java Programming (Liang), 9.9: Data Field Encapsulation
- [Liang's Chapter 9 exercises, with solutions](https://github.com/HarryDulaney/intro-to-java-programming/tree/master/ch_09)
