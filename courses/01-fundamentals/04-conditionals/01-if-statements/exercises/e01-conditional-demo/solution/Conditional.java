public class Conditional {
    public static void main(String[] args) {
        // --- The if Statement ---
        int r = -2;
        if (r <= 0) {
            System.out.println("Retype radius above 0");
        }
        System.out.println("Runs regardless");

        // --- if / else ---
        double radius = 1.0;
        if (radius <= 0) {
            System.out.println("Retype radius above 0");
        } else {
            System.out.println(radius * radius * 3.14); // area of the circle
        }

        // --- else if ---
        int age = 22;
        if (age >= 16) {
            System.out.println("You can drive");      // the first true branch wins...
        } else if (age >= 21) {
            System.out.println("You can rent a car"); // ...so this can never run
        } else {
            System.out.println("You cannot drive");
        }

        // Most specific condition first
        if (age >= 21) {
            System.out.println("You can rent a car");
        } else if (age >= 16) {
            System.out.println("You can drive");
        } else {
            System.out.println("You cannot drive");
        }

        // --- Nested if Statements ---
        boolean hasID = true;
        if (age >= 18) {
            if (hasID) {
                System.out.println("Entry allowed.");
            } else {
                System.out.println("Old enough, but ID required.");
            }
        } else {
            System.out.println("Not old enough");
        }

        // The same logic, flattened with &&
        if (age >= 18 && hasID) {
            System.out.println("Entry allowed.");
        } else if (age >= 18 && !hasID) {
            System.out.println("Old enough, but ID required.");
        } else {
            System.out.println("Not old enough");
        }

        // --- Guarding Against Errors ---
        int dividend = 10;
        int divisor = 0;
        if (divisor != 0 && dividend / divisor == 2) { // && skips the division when divisor is 0
            System.out.println("Runs");
        } else {
            System.out.println("Error: divide by zero.");
        }

        double total = 0.1 + 0.2;
        if (Math.abs(total - 0.3) < 1e-9) {
            System.out.println("Total is close enough.");
        }

        // --- Common Traps ---
        // Missing braces: only the NEXT line belongs to the if
        boolean loggedIn = false;
        if (loggedIn)
            System.out.println("Welcome Back!");
            System.out.println("This prints even though loggedIn is false");

        // Stray semicolon: the ; IS the whole if statement
        int n = -5;
        if (n > 0); // <- this semicolon
        {
            System.out.println("This prints, even though n is -5");
        }

        // = instead of ==: won't compile, the condition must be a boolean
        // if (n = 5) { }
    }
}
