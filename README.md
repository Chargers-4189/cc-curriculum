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
│   ├── lms/published.json               # what was last uploaded to each page
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

Slides are optional. Fundamentals is the only course with them right now, but you can add them to any course.

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
ccm update               # refresh material and ccm itself
```

Students receive lectures, slides, readings, practice and exercise starter code. Instructors can add `-i` to `ccm get` to include lecture notes and quizzes. Solutions are never downloaded.

`ccm test` needs Java 17+.

<!-- Note for students on where to put their work / how exercises are submitted on the LMS. -->

## For Instructors

### Adding content

Run these from a clone of the repo. Each one copies a template and picks the next number for you:

```bash
tools/ccm new chapter 1 control-flow
tools/ccm new lesson 1.2 if-statements
tools/ccm new exercise 1.2.1 grade-calculator
```

If an exercise doesn't need tests, you can delete its `tests/` and `solution/` folders.

### Exercises

Each `prompt.md` has a `type` at the top:

| Type | Where it shows up |
|------|-------------------|
| `follow-along` | The lesson's **Follow Along** section, students fill it in as they read |
| `practice` | A code playground on the lesson page |
| `homework` | Its own assignment page after the lesson |

Practice and homework always use `public class Main` since that's what the Charging Courses code editor runs. This also lets students copy their code between Labs and the site.

Tests go in `tests/cases.csv` (`label,input,output,hidden`), and both the site and `ccm test` use them. After editing one, run `python3 tools/cases.py` to update `MainTest.java`. The easiest way to fill in `output` is to run the solution and paste what it prints.

### Quizzes

Each lesson's quiz is `quiz/review.csv`, with one question per line:

| question | answer | incorrect_1 | incorrect_2 | incorrect_3 |
|---|---|---|---|---|
| What is 17 % 5? | 2 | 3 | 3.4 | 85 |

For select all that apply questions, add `answer_2` and `answer_3` columns and leave them blank on the other questions. Add the quiz to a lesson with `[Quiz](quiz/review.csv)`.

Practice sets can also go in `practice/practice.yaml` (`mc`, `tf`, `short`, `long`, `code-output`, `flashcard`). To print a quiz with an answer key, run `python3 tools/export/quiz.py 1.2.1`.

### Check-ins

Each course has 3 graded check-ins in `courses/<course>/check-ins/`. They show up as assignments right after the lesson in `after:` and grade themselves.

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

Everything is worth 10 points unless you set `points:`.

### Publishing to Charging Courses

Always make your changes here first, then publish them to the site.

To set it up, install the requirements and put your API token in `.env` as `CC_API_TOKEN=lh_...`. You can make a token in Dashboard → Developers → API Access, with create, read, and update for courses, chapters, activities, and assignments.

```bash
pip install -r tools/requirements.txt
python3 tools/lms/publish.py --dry-run     # see what would change
python3 tools/lms/publish.py               # update every course on the site
python3 tools/lms/publish.py courses/01-fundamentals/05-loops/01-while-loops   # just one lesson
python3 tools/lms/publish.py courses/02-object-oriented                        # make a new course
```

A few things to know:

- New courses start unpublished so you can look them over. New lessons, homework, and check-ins are published right away.
- If someone changed a page on the site, it won't get overwritten. You'll see what's different so you can copy it into the repo, or use `--force` to replace it.
- Images have to be added in the editor. New pages will have a note where each image goes.
- In a lesson, `{{user.first_name}}` shows the student's name and `[General](community:community_<uuid>)` links to a community.
- Commit `tools/lms/ids.yaml` and `tools/lms/published.json` after you publish.

### Checks

```bash
pip install -r tools/requirements.txt
python tools/validate/validate.py     # structure, front matter, quizzes, links
tools/check-exercises.sh              # exercise tests pass against solutions
```

CI runs these on every push and pull request.

### Releases

Tagging a version (like `v2026.1`) makes a release with the exported quizzes and slide PDFs. `ccm` downloads the latest release, so changes on `main` won't affect students in the middle of a course.

<!-- Release schedule / who tags releases. -->

## Contributing

<!-- Who can contribute, branch/PR process, review expectations. -->

## Credits and License

See [CREDITS.md](CREDITS.md) for authors and sources. Released under the [MIT License](LICENSE).
