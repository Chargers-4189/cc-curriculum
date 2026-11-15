# Charging Courses Curriculum Mono-repository

This repository contains all lesson materials, exercises, solutions, quizzes, practices, and scripts for Charging Courses students. Instructors should use this as the primary source of information and a mirror for content published on the LMS.

## Courses

| # | Course | Description |
|---|--------|-------------|
| 0 | START HERE | Prerequisite information and navigating Charging Courses |
| 1 | Fundamentals | Introduction to Java and basic programming concepts |
| 2 | Object Oriented | Object-Oriented Programming and software architecture |
| 3 | WPILib | WPILib libraries and software (Planned) |
| 4 | Robot Programming | Programming subsystems and commands (Planned) |
| 5 | Workshops | Individualized lesson material on specific content (Planned) |

Content is organized the same way as the LMS: **course → chapter → lesson**.

## Repository Layout

```
cc-curriculum/
├── courses/
│   ├── 00-start-here/
│   ├── 01-fundamentals/
│   │   ├── course.yaml                  # course title, options
│   │   ├── check-ins/                   # graded check-ins (YAML)
│   │   └── 01-<chapter>/
│   │       ├── chapter.yaml             # chapter title
│   │       └── 01-<lesson>/
│   │           ├── lecture.md           # main lecture (key points)
│   │           ├── lecture-notes.md     # spoken notes for the lecture
│   │           ├── slides.md            # slides (optional)
│   │           ├── reading.md           # supporting reading
│   │           ├── quiz/review.csv      # review quiz: question, answer, incorrect answers
│   │           ├── practice/            # practice questions, flashcards, links
│   │           └── exercises/
│   │               └── e01-<exercise>/
│   │                   ├── prompt.md    # instructions (type: follow-along, practice or homework)
│   │                   ├── starter/     # code students start from (Main.java for practice/homework)
│   │                   ├── tests/       # cases.csv (input/output tests) + generated MainTest.java
│   │                   └── solution/    # reference solution
│   └── 02-object-oriented/
├── shared/
│   ├── templates/                       # skeletons used by `ccm new`
│   └── java-test-helpers/               # TestUtil.java, available to all exercise tests
├── tools/
│   ├── ccm                              # download / test / scaffold CLI
│   ├── validate/validate.py             # structure, front matter, quiz and link checks
│   ├── export/quiz.py                   # quiz/practice -> Markdown, answer keys, flashcards
│   ├── cases.py                         # tests/cases.csv -> tests/MainTest.java
│   ├── lms/publish.py                   # uploads everything to Charging Courses
│   ├── lms/build.py                     # turns a lesson into a Charging Courses page
│   ├── lms/ids.yaml                     # which page on the site each lesson is
│   ├── lms/published.json               # what was last published to each page
│   ├── lms/pull.py                      # copies site edits back into a lesson
│   ├── lms/forget.py                    # used by ccm remove
│   ├── move.py                          # used by ccm mv
│   └── check-exercises.sh               # runs every exercise's tests against its solution
├── .github/workflows/                   # CI and release automation
├── install.sh                           # one-line installer for ccm
├── CREDITS.md                           # authors, sources, citation
└── LICENSE
```

### Naming and addresses

- Courses, chapters and lessons are folders named `NN-name` (two-digit number, lowercase, hyphens). Exercises are `eNN-name`.
- The numbers set the order; the names must be unique across the repo for lessons and exercises.
- Every item has an address built from its numbers:

| Address | Refers to |
|---------|-----------|
| `1` | Course 1 (Fundamentals) |
| `1.2` | Chapter 2 of Fundamentals |
| `1.2.1` | Lesson 1 of that chapter |
| `1.2.1.e1` | Exercise 1 of that lesson |

Names work in place of numbers: `if-statements`, `1.2.if-statements.e1`.

### Lesson files

<!-- Describe what belongs in each file and how they're used in class. -->

| File | Required | Purpose |
|------|----------|---------|
| `lecture.md` | yes | <!-- --> |
| `lecture-notes.md` | no | <!-- --> |
| `reading.md` | no | <!-- --> |
| `slides.md` | no | <!-- --> |
| `quiz/` | no | <!-- --> |
| `practice/` | no | <!-- --> |
| `exercises/` | no | <!-- --> |

Slides are optional. Right now only Fundamentals has them, but any course can add them.

The templates include **Objectives**, **Prerequisites**, **Review**, and **Readings** (**Required** / **Further**) sections; keep the ones a lesson needs and delete the rest.

## Getting the Material

Install `ccm` (Linux/macOS, requires bash and curl):

```bash
curl -fsSL https://raw.githubusercontent.com/Chargers-4189/cc-curriculum/main/install.sh | bash
```

```bash
ccm list                 # show all courses, chapters and lessons
ccm list 1.2.1           # show one lesson and its exercises
ccm get 1.2.1            # download a lesson into the current folder
ccm get if-statements    # same, by name
ccm test                 # test the exercise(s) in the current folder
ccm test 1.2.1.e1        # test a specific exercise from anywhere nearby
ccm search loops         # find a lesson or exercise
ccm show 1.2.1.e2        # read an exercise's instructions in the terminal
ccm open 1.2.1           # open that lesson (or homework) on Charging Courses
ccm doctor               # check that everything ccm needs is working
ccm update               # refresh material and ccm itself
```

Students get the lectures, slides, readings, practice, and exercise starter code, but no solutions. `ccm test` needs Java 17+.

If you leave out the address (like `ccm get` or `ccm show`), you'll get a list to pick from. You can type to search it. If `ccm test` can't find an exercise in the folder you're in, it lists the ones you've downloaded so you can pick one.

`ccm` uses [gum](https://github.com/charmbracelet/gum) for its menus. If you don't have it, `ccm` downloads it the first time it needs it (about 14 MB, into its cache). To use plain prompts instead, set `CCM_NO_GUM=1`.

`ccm help` only shows the student commands. To see the instructor commands too, run it inside a clone of the repo or run `ccm instructor on`.

<!-- Note for students on where to put their work / how exercises are submitted on the LMS. -->

## For Instructors

### Instructor commands

These only work inside a clone of the repo. The first time you use one that needs Python, `ccm` will set it up in `.venv`. You can run `ccm doctor` to check your setup.

```bash
ccm add                              # add a course, chapter, lesson, exercise or check-in, step by step
ccm new lesson 1.2 if-statements     # same thing in one line (also: course, chapter, exercise)
ccm mv 1.5.2 counting-loops          # rename (or: ccm mv 1.5.2 1 to make it first, --into 1.6 to move it)
ccm rm 1.2.3                         # delete a course, chapter, lesson or exercise
ccm get -i 1.2.1                     # download a lesson with its lecture notes and quizzes
ccm validate                         # check structure, quizzes, links, check-ins
ccm check                            # run every exercise's tests against its solution
ccm cases --fill                     # fill in empty outputs in cases.csv by running the solution
ccm export 1.2.1                     # print a quiz with an answer key
ccm publish --dry-run                # see what would change on Charging Courses
ccm pull                             # see which pages were changed on the site
ccm release --dry-run                # check what students would get in the next release
```

`ccm add` will ask you what you want to add, where it goes, the title, and which files to include, then make it from the templates. If the name you type is already used somewhere, it tells you where and asks again. You can also type a title like `While Loops` and it'll turn it into `while-loops`. `ccm new` does the same thing in one line. If an exercise doesn't need tests, you can delete its `tests/` and `solution/` folders.

If you leave out the address for `ccm mv`, `ccm rm`, or `ccm pull`, you'll get a list to search and pick from.

`ccm mv` also updates the links in other lessons, the `ccm get` lines, the check-ins, and `tools/lms/ids.yaml`, and the next publish moves the page on the site too. The addresses students use will change, so it's best to rename things before a course starts.

`ccm rm` will show you what it's deleting and what links to it, then ask you to type the name to confirm. It only deletes things in the repo, so you will need to remove the page on Charging Courses yourself.

### Exercises

Each `prompt.md` has a `type` at the top:

| Type | Where it shows up |
|------|-------------------|
| `follow-along` | The lesson's **Follow Along** section, students fill it in as they read |
| `practice` | A code playground on the lesson page |
| `homework` | Its own assignment page after the lesson |

Practice and homework always use `public class Main` because that's what the Charging Courses code editor runs. Students can then copy their code between Labs and the site.

Tests go in `tests/cases.csv` (`label,input,output,hidden`). The site and `ccm test` both use them. After you edit one, run `ccm cases` to update `MainTest.java`. If you leave `output` empty, `ccm cases --fill` will fill it in by running the solution.

### Quizzes

Each lesson's quiz is `quiz/review.csv`, with one question per line:

| question | answer | incorrect_1 | incorrect_2 | incorrect_3 |
|---|---|---|---|---|
| What is 17 % 5? | 2 | 3 | 3.4 | 85 |

For select all that apply questions, add `answer_2` and `answer_3` columns and leave them blank for the other questions. To add the quiz to a lesson, put `[Quiz](quiz/review.csv)` where you want it.

Practice sets can also go in `practice/practice.yaml` (`mc`, `tf`, `short`, `long`, `code-output`, `flashcard`).

### Check-ins

Each course has 3 graded check-ins in `courses/<course>/check-ins/`. Each one is an assignment that goes right after the lesson in `after:`, and it's graded automatically.

```yaml
title: "Check-in 1"
after: 03-operators/02-relational-and-logical-operators
description: |
  Covers Basics of Computers through Relational and Logical Operators.
tasks:
  - type: quiz              # use answers: [...] for select all that apply
    questions:
      - question: "What does the Java compiler create?"
        answer: "A class file (bytecode)"
        incorrect: ["A source file", "An .exe file"]
  - type: number
    prompt: "What does System.out.println(17 / 5 + 17 % 5); print?"
    answer: 5
  - type: short             # not case sensitive
    prompt: "What command compiles HelloWorld.java?"
    answers: ["javac HelloWorld.java"]
  - type: fill-in
    questions:
      - text: "Declare an int named age:  ___ age = 16;"
        blanks: [{answer: "int", hint: "type"}]
```

Each question is worth 10 points unless you set `points:`.

### Publishing to Charging Courses

Please make your changes here first, then publish them to the site.

To set it up, make an API token in Dashboard → Developers → API Access with create, read, and update for courses, chapters, activities, and assignments. Then put it in `.env` as `CC_API_TOKEN=lh_...`.

```bash
ccm publish --dry-run     # see what would change
ccm publish               # update every course on the site
ccm publish courses/01-fundamentals/05-loops/01-while-loops   # just one lesson
ccm publish courses/02-object-oriented                        # make a new course
```

Some things to know:

- New courses are unpublished at first so you can look them over. New lessons, homework, and check-ins are published right away.
- If someone edited a page on the site, publishing will skip it. Run `ccm pull 1.2.1` to copy those edits into the repo, or use `--force` to replace them.
- Images have to be added in the editor. New pages will have a note where each image goes.
- In a lesson, `{{user.first_name}}` shows the student's name and `[General](community:community_<uuid>)` links to a community.
- Commit `tools/lms/ids.yaml` and `tools/lms/published.json` after you publish.

### Checks

`ccm validate` and `ccm check` also run on every push and pull request.

### Releases

Students download from the latest release, so they won't see new material until you make a new one. Run `ccm release` from `main`. It will run the checks, show you what changed, then tag and push the next version (like `v2026.1`). GitHub then builds the release with the exported quizzes and slide PDFs.

<!-- Release schedule / who tags releases. -->

## Contributing

<!-- Who can contribute, branch/PR process, review expectations. -->

## Credits and License

See [CREDITS.md](CREDITS.md) for authors and sources. Released under the [MIT License](LICENSE).
