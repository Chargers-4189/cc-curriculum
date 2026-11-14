## What is Java

- Created 1995 by Sun Microsystems, now Oracle
- High-level: written for humans to read; the compiler handles the machine side
- WORA: the JVM is what makes "run anywhere" possible; same code on Windows, Mac, Linux, roboRIO
- Android as the real-world example; also mention our robot code is Java (WPILib)

## The Four Steps

- Source file (`.java`) → compiler (`javac`) → class file (`.class`, bytecode) → runtime (JVM, `java`)
- Analogy from the diagram: you write a document, a printer turns it into something another machine reads, then that machine follows it
- Live demo in the terminal: `javac`, then `ls` to show the new `.class` file, then `java`
- Point out the Run button does exactly these two steps

## Code Structure

- Boxes in boxes: source file ⊃ class ⊃ method ⊃ statements
- Walk through the labeled slide piece by piece
- Don't go deep on `public static void` and `String[] args`; say "we'll come back to these"
- Semicolons end statements; braces open and close blocks

## main()

- The JVM looks for `main` and starts there
- No `main` = nothing to run (show the error if time allows)

## Check for Understanding

- "What file does `javac Main.java` create?"
- "If I delete `Main.class`, can I still run the program?" (not until you compile again)
