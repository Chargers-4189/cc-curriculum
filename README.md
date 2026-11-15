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
│   ├── lms/build.py                     # lesson/homework -> Charging Courses page content
│   ├── lms/ids.yaml                     # which Charging Courses page each lesson/homework is
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
| `slides.md` | Fundamentals only | <!-- --> |
| `quiz/` | no | <!-- --> |
| `practice/` | no | <!-- --> |
| `exercises/` | no | <!-- --> |

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

Run from a clone of this repo; each command copies the matching template and picks the next number:

```bash
tools/ccm new chapter 1 control-flow
tools/ccm new lesson 1.2 if-statements
tools/ccm new exercise 1.2.1 grade-calculator
```

Exercises that don't need automatic checking can delete their `tests/` and `solution/` folders.

### Exercise types

Each exercise's `prompt.md` front matter has a `type`:

| Type | On Charging Courses | Files |
|------|---------------------|-------|
| `follow-along` | Described in the lesson's **Follow Along** section; students fill it in while reading | `starter/` and `solution/` with a descriptive class name (`Variables.java`) |
| `practice` | A **code playground** on the lesson page | `starter/Main.java`, `solution/Main.java`, `tests/cases.csv` |
| `homework` | Its own **assignment** page with a code task | same as practice; `tests/` is optional (e.g. random programs) |

Practice and homework always use `public class Main`, because the LMS code editor runs `Main.java`. That way students can copy their code between Labs and Charging Courses.

`tests/cases.csv` holds the tests (`label,input,output,hidden`). The same rows become the playground/assignment tests on the LMS and the JUnit tests `ccm test` runs. Output must match exactly, except spaces at the end of a line and blank lines at the end. After editing a `cases.csv`, regenerate the JUnit file:

```bash
python3 tools/cases.py
```

The easiest way to get the `output` column right is to run the solution and paste what it prints (the prompts end up on one line with the answer, since typed input isn't shown).

### Quizzes and practice

Each lesson's review quiz is `quiz/review.csv`, one multiple-choice question per row:

| question | answer | incorrect_1 | incorrect_2 | incorrect_3 |
|---|---|---|---|---|
| What is 17 % 5? | 2 | 3 | 3.4 | 85 |

For a **select all that apply** question, add `answer_2`, `answer_3`, ... columns after `answer` (leave them empty on single-answer rows):

| question | answer | answer_2 | incorrect_1 | incorrect_2 |
|---|---|---|---|---|
| Which of these are primitive types? (select all that apply) | int | boolean | String | Scanner |

Keep each question on one line. The lesson links to it with `[Quiz](quiz/review.csv)`, which becomes an Interactive Quiz on the LMS.

Practice sets can still be written in YAML (`practice/practice.yaml`) with types `mc`, `tf`, `short`, `long`, `code-output`, and `flashcard`.

```bash
python tools/export/quiz.py 1.2.1     # -> build/quizzes/: student copy, answer key, flashcards.tsv
```

### Check-ins

Each course has 3 graded **check-ins**, written as YAML in `courses/<course>/check-ins/`. Each one becomes an auto-graded assignment placed right after the lesson in its `after:` line:

```yaml
title: "Check-in 1"
after: 03-operators/02-relational-and-logical-operators
description: |
  Covers Basics of Computers through Relational and Logical Operators.
tasks:
  - type: quiz            # multiple choice; use answers: [..] for select all that apply
    questions:
      - question: "What does the Java compiler create?"
        answer: "A class file (bytecode)"
        incorrect: ["A source file", "An .exe file"]
  - type: number          # a numeric answer (optional tolerance, unit)
    prompt: "What does System.out.println(17 / 5 + 17 % 5); print?"
    answer: 5
  - type: short           # short text, matched ignoring case
    prompt: "What command compiles HelloWorld.java?"
    answers: ["javac HelloWorld.java"]
  - type: fill-in         # fill in the blanks
    questions:
      - text: "Declare an int named age:  ___ age = 16;"
        blanks: [{answer: "int", hint: "type"}]
```

Points default to 10 per question, answer, or blank (`points:` overrides it).

### Site-only blocks in lessons

- `{{user.first_name}}` shows the student's own name. `{{user.full_name|capitalize|there}}` is path, format, and fallback.
- `[General](community:community_<uuid>)` links to a community.

### Publishing to Charging Courses

`tools/lms/build.py` turns a lesson into the LMS editor's format: callouts, tables and code blocks become LearnHouse blocks, `[Quiz](quiz/review.csv)` becomes an Interactive Quiz, each practice link becomes a code playground, homework links and lesson links point at their Charging Courses pages (from `tools/lms/ids.yaml`), and images reuse the ones already uploaded to that page.

```bash
pip install -r tools/requirements.txt
python3 tools/lms/build.py courses/01-fundamentals/02-java-basics/02-hello-world -o build/lms
python3 tools/lms/build.py --homework courses/.../exercises/e05-day-of-week -o build/lms
```

The JSON it writes is the page's `content` (or an assignment and its code task) for the LearnHouse API.

**Edit the repo first, then publish.** Changes made only on the site get overwritten the next time someone publishes, so make them here.

To upload to the site, use `tools/lms/publish.py`. It rebuilds every lesson, homework, and check-in, updates the pages that are different, and creates anything that isn't on the site yet (lessons, homework, check-ins, chapters, or a whole course), saving the new ids in `ids.yaml`:

```bash
python3 tools/lms/publish.py --dry-run     # see what would change
python3 tools/lms/publish.py               # update every course that's on the site
python3 tools/lms/publish.py courses/02-object-oriented                        # create or update one course
python3 tools/lms/publish.py courses/01-fundamentals/05-loops/01-while-loops   # just one lesson
```

- A new course is only created when you name its folder, and it starts **unpublished** so you can look it over first. New lessons and homework are published right away and placed in repo order.
- Names come from `course.yaml` / `chapter.yaml` titles, lesson folder names (`02-for-loops` → "For Loops"), and "*Title* (Homework)". Renaming on the site is safe; publishing never changes names.
- If a page with the same name already exists in that chapter, it's linked instead of duplicated.
- API tokens can't upload images, so a new page gets a note where each image goes. Add the image there in the editor, delete the note, and the next run picks it up.
- A page is skipped, not overwritten, if its image count doesn't match the markdown or it has blocks the markdown can't make (like a video added on the site). `--force` overrides that.

It needs an API token (Dashboard → Developers → API Access, with create, read and update rights for courses, chapters, activities and assignments) in `.env` at the top of the repo as `CC_API_TOKEN=lh_...` (git ignores `.env`).

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
