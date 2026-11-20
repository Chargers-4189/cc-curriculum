---
title: "Ticket Machine"
type: practice
difficulty: easy
---

Every `Ticket` gets the next number: the first one made is #1, the second is #2, and so on. `main` is already written. Write the `Ticket` class:

- A **private static** `int ticketsSold` that counts every ticket made
- A **private final** `int number` for this ticket's number
- A no-arg constructor that counts the new ticket and gives it its number
- `getNumber()`, which gives back this ticket's number
- A **static** `getTicketsSold()`, which gives back how many tickets have been made

```
Sold so far: 0
First ticket: #1
Second ticket: #2
Third ticket: #3
Sold so far: 3
```

**Hint:** `ticketsSold` is shared by every ticket, but `number` belongs to each one.

## In Labs

Prefer to work in Charging Courses Labs? Download it, write your code in `Main.java`, and check it:

```bash
ccm get ticket-machine
cd ticket-machine
ccm test
```
