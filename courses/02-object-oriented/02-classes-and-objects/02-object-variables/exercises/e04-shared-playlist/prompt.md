---
title: "Shared Playlist"
type: homework
difficulty: medium
---

The `Playlist` class is already written at the bottom of the file. A playlist knows its `name` and its `songCount`, and `addSong()` adds one to its song count. `new Playlist("Road Trip")` makes a playlist named Road Trip with 0 songs.

Write `main`. Draw the memory map as you go, it makes this a lot easier.

**Part 1**

1. Make a playlist named `Road Trip` in a variable called `roadTrip`.
2. Make a variable called `shared` that refers to the **same** playlist. Don't make a new one.
3. Add two songs through `shared`, then one song through `roadTrip`.
4. Make a playlist named `Gym` in a variable called `gym` and add two songs to it.
5. Print `roadTrip`, then `shared`, then `gym`, each on its own line, like this:

```java
System.out.println(roadTrip.name + ": " + roadTrip.songCount + " songs");
```

**Part 2**

6. Make `shared` refer to the Gym playlist.
7. Add one song through `shared`.
8. Print `roadTrip`, `shared` and `gym` again.

The full output:

```
Road Trip: 3 songs
Road Trip: 3 songs
Gym: 2 songs
Road Trip: 3 songs
Gym: 3 songs
Gym: 3 songs
```

**Hints:**
- There are only ever **two** playlists. `shared` isn't a playlist, it's a way to get to one.
- If your Road Trip count is wrong, check that step 2 doesn't use `new`.

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get shared-playlist
cd shared-playlist
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
