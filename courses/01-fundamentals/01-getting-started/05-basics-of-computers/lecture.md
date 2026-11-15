> **Objectives**
> - Explain what programming is and why it's useful
> - Tell the difference between hardware and software
> - Describe the Computer Model: input, storage, processing, output
> - Compare primary and secondary storage
> - Understand files, folders, repositories, and IDEs
>
> **Prerequisites:** None! This is where we start.

## What is Programming

Programming is a way of giving computer instructions.

- Programming is in every technological device
- Computers take things literally. You must be very specific about your instructions.
- People have been finding the best way to communicate to a computer
- We continue to develop coding languages to better communicate with computers, like Java, Python, C++, and HTML

## How is Programming Useful

- **Automation** of machinery and processes
- **Controlling** of our robot
- **Communication** between controls, motors, and other components
- Programming allows us to give **detailed instructions** on what to do

Humans and computers are good at very different things. That's why we program: we bring the creativity, the computer brings the speed and consistency.

| Human | Computer |
|---|---|
| Thinks creatively | No creativity (follows given instructions) |
| Communicates through inference | Limited, hard-wired knowledge |
| Detects patterns to make sense of the world | Calculates information quickly |
| Inconsistent (prone to human error) | Consistent (accurate) |
| Can get bored or distracted | Does not lose focus |

## Computers

- **Hardware** is the physical components: CPU, RAM, etc.
- **Software** is stored instructions: operating systems, code, etc.

Computers come in many forms:

- **Desktops** are powerful computers used at home, work, or school, usually on a desk
- **Tablets, laptops, and phones** are rechargeable handheld/portable computers
- **Servers** provide information to others. Your workspace runs on a server!

Computers process information and give outputs. This simple operation is what makes complex applications possible.

## The Computer Model

The Computer Model shows how a computer works:

- **Input Devices** collect information from users: keyboards, mice, sensors
- **Storage Devices** store information: external drives, flash media
- **Processing Devices** process information: the CPU in laptops and desktops
- **Output Devices** output information: motors, speakers, printers

Notice the robot fits this model too. Sensors and controllers are inputs, the roboRIO processes, and motors are outputs.

## Memory

Memory comes in two broad categories:

- **RAM & ROM** - Primary storage, temporary
- **HDD & SSD** - Secondary storage, permanent

**Random Access Memory (RAM)** is the fastest memory.

- It is cleared when the computer turns off
- It holds active memory for programs that are running
- Programs are unloaded from RAM to save space

**Secondary storage** is permanent but slower.

- Programs and files are stored here when they're not in RAM

## Files

There are many types of files:

- **Document files:** pdf, word, xlsx, ppt, txt, md...
- **Media files:** png, mp4, mp3, gif, jpg...
- **Program files:** html, py, css, js, java...

Files are usually named with their format at the end: `nameOfFile.format`, e.g. `cat.png`, `movie.mp4`, `index.html`.

All programs and data are **written to** or **read from** a file.

## Folders

Folders (or directories) are an organizational tool used to arrange files so you can store them neatly.

- They can hold many different types of files
- They can be named to quickly identify contents
- They can be put within each other

```
Folder_1/
├── File.png
├── cat.jpg
└── alice.gif

Folder_2/
├── Folder_1/
│   ├── animation.gif
│   └── music.mp3
├── index.html
└── logo.png

Folder_3/
└── spark.mp4
```

Some folders are specialized to hold code. These are called **repositories**. They help **track code** and **record who changed what and when**. We'll use them with GitHub later on.

## IDE

**Integrated Development Environments** are tools that have most of what is needed to develop code:

- **Text Editor** - writing the code
- **Repository** - storing the code
- **Runtime Environment** - running the code
- **Deployment Method** - deploying the code

Examples are VS Code, Eclipse, and Repl.it. We use VS Code, both in your workspace and on the robot.

## Review Quiz

[Basics of Computers Quiz](quiz/review.csv)
