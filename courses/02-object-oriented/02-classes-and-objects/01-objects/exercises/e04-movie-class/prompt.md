---
title: "Movie Class"
type: homework
difficulty: easy
---

`main` is already written. It makes two movies and uses them. Your job is the `Movie` class at the bottom of the file.

A `Movie` **knows**:

- `title` (a `String`)
- `genre` (a `String`)
- `rating` (an `int`)

A `Movie` **does** one thing: `playIt()`, which prints `Playing the movie ` followed by its title.

When it works, the program prints:

```
Playing the movie Iron Lung
Playing the movie Toy Story 5
Iron Lung is rated 9
Toy Story 5 is a Comedy movie
```

**Hints:**
- Look at the `Cat` class from the lesson. `Movie` is set up the same way.
- The instance variables don't get values in the class. `main` gives each movie its own.
- Your variable names have to match the ones `main` uses: `title`, `genre`, `rating`.

*Adapted from the Movie example in Head First Java (Sierra, Bates & Gee), Chapter 2.*

## In Labs

Download it, write your code in `Main.java`, and check it:

```bash
ccm get movie-class
cd movie-class
ccm test
```

When it works, copy **all** of `Main.java` into the assignment on Charging Courses and hand it in.
