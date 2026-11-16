## Setup (5 min)

- Split the room in half. Team A: `ccm get shape-wars-team-a`. Team B: `ccm get shape-wars-team-b`
- Don't tell either team what the other file looks like, and keep the lesson page closed until the debrief (it has both teams' code)
- Before they open anything, say it out loud: this works, it's tested, don't touch it until I read a spec change
- Both run it; the output is the same
- Scoring is **not speed**. It's lines of already-working code you had to touch. Say it twice. A new class or file costs 0, editing a working line costs 1
- Put the scoreboard on the board. Let them argue about the count, the arguing is good
- When we ran it: Team A 7 + 11 = 18, Team B 14 + 1 = 15. Team B counted their new lines on change 1, so be clear about the rule up front

## Read Your Own Code (5 min)

- On paper: where do I look for everything about the circle? Where does a shape's width live?
- Team A: scattered across four `switch`es. Team B: in `Circle`, two lines
- Don't comment yet, just collect the answers

## Spec Change 1 (15 min)

- Read it with as much Annoying Project Manager energy as you can
- Team A: edits `getName`, `getWidth`, `getHeight`, `playSound`, a new constant, the clicks array. Around 6
- Team B: one new class, two lines in main. Around 2
- Team A often finishes first since the edits are mechanical. Let them enjoy it

## Spec Change 2 (15 min)

- This is the one that hurts
- Team A: `if (shapeNum == AMOEBA)` in `rotate`, or a new signature that breaks every call. Let them find this out, and make them actually do one
- Team B: `xPoint` and `yPoint` in `Amoeba`, one method body. Nothing tested gets touched
- Rough final: Team A ~12, Team B ~0

## Team A Fights Back (5 min)

- Ask Team A: what's wrong with Team B's four classes?
- `rotate()` and `playSound()` are written four times. Team A is right, say so
- Draw the `Shape` diagram. Define override in one sentence and stop; inheritance is a later lesson
- Leave the `Shape[]` loop on the board

## Debrief (10 min)

Get these out of them in their words:

- Which team ever broke a working shape? Only A could, only A edited working shapes
- Where does a circle's width live in each version?
- What's an object? Knows things (instance variables), does things (methods). Point at `Amoeba`
- Class vs object: blueprint vs `new Amoeba()`
- End on: procedural is organized around what the program does, OO around what it's made of

## Notes

- Finished early: make them write a `Star`. Team B does it in 90 seconds, Team A sighs
- "The OO version is longer": they're right. Longer at the start, flatter over time
- Don't say "encapsulation" yet; the variables are wide open and that's fine today
- `TeamB.java` has to keep its name. New classes go at the bottom, no `public`
- Missed class or fell behind: the four Spec Change playgrounds on the lesson page start from the right code for each team
