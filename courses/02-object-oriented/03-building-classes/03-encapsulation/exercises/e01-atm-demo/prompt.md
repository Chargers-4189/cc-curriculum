---
title: "ATM (Follow Along)"
type: follow-along
---

Follow along with the lesson in `ATM.java` and `ATMDriver.java`. Each section of the lesson has matching `// --- Section ---` comments.

1. Break the ATM: withdraw a negative amount, then set the balance directly.
2. Make `balance` and `name` `private`, and see what stops compiling.
3. Make `deposit` and `withdraw` check the amount before they change the balance.
4. Add getters for the name and balance, but no setters.

## In Labs

```bash
ccm get atm-demo
cd atm-demo
```

Run `ATMDriver` with the Run button, or:

```bash
javac *.java
java ATMDriver
```
