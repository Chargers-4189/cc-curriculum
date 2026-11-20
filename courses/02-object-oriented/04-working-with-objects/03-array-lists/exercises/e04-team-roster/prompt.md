---
title: "Team Roster"
type: homework
difficulty: medium
---

Keep track of who's on a drive team. Store the names in an `ArrayList<String>` and read commands until the user types `quit`:

| Command | What it does |
|---|---|
| `add <name>` | Adds the name and prints `Added <name>`. If they're already on the team, print `<name> is already on the team`. If the team already has `MAX_TEAM_SIZE` (4) people, print `The team is full` |
| `remove <name>` | Removes the name and prints `Removed <name>`, or prints `<name> isn't on the team` |
| `list` | Prints `Team: ` and then the whole list, like `Team: [Quinn, Caleb]` |
| `count` | Prints how many are on the team out of the max, like `2 of 4` |
| `quit` | Prints `Bye!` and ends |
| anything else | Prints `Unknown command: <command>` |

Names are one word. For example, if the user types:

```
add Quinn
add Caleb
add Quinn
list
remove Bryan
remove Caleb
count
quit
```

the program prints:

```
Added Quinn
Added Caleb
Quinn is already on the team
Team: [Quinn, Caleb]
Bryan isn't on the team
Removed Caleb
1 of 4
Bye!
```

**Hints:**
- Read the command with `input.next()`. For `add` and `remove`, read the name with another `input.next()`.
- `contains` tells you if a name is already there.
- `remove(name)` gives back `true` if it found and removed the name, and `false` if it wasn't there.
- Printing an ArrayList prints it in brackets for you: `System.out.println("Team: " + team);`

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get team-roster
cd team-roster
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
