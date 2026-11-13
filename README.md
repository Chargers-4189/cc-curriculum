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
│   │   └── 01-<chapter>/
│   │       ├── chapter.yaml             # chapter title
│   │       └── 01-<lesson>/
│   │           ├── lecture.md           # main lecture (key points)
│   │           ├── lecture-notes.md     # spoken notes for the lecture
│   │           ├── slides.md            # slides (Fundamentals only)
│   │           ├── reading.md           # supporting reading
│   │           ├── quiz/quiz.yaml       # quiz questions + answers
│   │           ├── practice/            # practice questions, flashcards, links
│   │           └── exercises/
│   │               └── e01-<exercise>/
│   │                   ├── prompt.md    # instructions
│   │                   ├── starter/     # code students start from
│   │                   ├── tests/       # optional automatic tests (JUnit)
│   │                   └── solution/    # reference solution
│   └── 02-object-oriented/
├── shared/
│   ├── templates/                       # skeletons used by `ccm new`
│   └── java-test-helpers/               # TestUtil.java, available to all exercise tests
├── tools/
│   ├── ccm                              # download / test / scaffold CLI
│   ├── validate/validate.py             # structure, front matter, quiz and link checks
│   ├── export/quiz.py                   # quiz/practice -> Markdown, answer keys, flashcards
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
| `lecture-notes.md` | yes | <!-- --> |
| `reading.md` | yes | <!-- --> |
| `slides.md` | Fundamentals only | <!-- --> |
| `quiz/` | no | <!-- --> |
| `practice/` | no | <!-- --> |
| `exercises/` | no | <!-- --> |

`lecture.md` and `reading.md` must contain these sections: **Objectives**, **Prerequisites**, **Review**, and **Readings** (with **Required** and **Further**).

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

Run from a clone of this repo; each command copies the matching template and picks the next number:

```bash
tools/ccm new chapter 1 control-flow
tools/ccm new lesson 1.2 if-statements
tools/ccm new exercise 1.2.1 grade-calculator
```

Exercises that don't need automatic checking can delete their `tests/` and `solution/` folders.

### Quizzes and practice

Questions are written in YAML (`quiz/quiz.yaml`, `practice/practice.yaml`) with types `mc`, `tf`, `short`, `long`, `code-output`, and `flashcard` (practice only). See `shared/templates/lesson/quiz/quiz.yaml` for the format.

```bash
python tools/export/quiz.py 1.2.1     # -> build/quizzes/: student copy, answer key, flashcards.tsv
```

<!-- How exported quizzes get into Google Forms / the LMS. -->

### Checks

```bash
pip install -r tools/requirements.txt
python tools/validate/validate.py     # structure, front matter, quizzes, links
tools/check-exercises.sh              # exercise tests pass against solutions
```

CI runs these on every push and pull request.

### Releases

Tagging a version (e.g. `v2026.1`) publishes a release with exported quizzes and slide PDFs. `ccm` downloads the latest release by default, so edits on `main` don't affect students mid-course.

<!-- Release schedule / who tags releases. -->

## Contributing

<!-- Who can contribute, branch/PR process, review expectations. -->

## Credits and License

See [CREDITS.md](CREDITS.md) for authors and sources. Released under the [MIT License](LICENSE).
