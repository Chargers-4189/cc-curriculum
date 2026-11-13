public class Conditional {
    public static void main(String[] args) {
        // Basic if
        if (true /* condition */) {
            /* code ran if condition is true */
        }

        if (false) {
            System.out.println("Hello World");
        }
        // System.out.println("Hi!");

        int age = 22;
        if (age >= 16) {
            System.out.println("You can drive");
        } else if (age >= 21) {
            System.out.println("You can rent a car");
        } else {
            System.out.println("You cannot drive");
        }

        /*
         * If statements take conditionals and run a section
         * of code if it is true. Else statements run only if
         * the if statement conditional resulted in FALSE. Else
         * if only runs if the previous statement was false AND
         * the current conditional returns TRUE. Else statement
         * will always run if none of the conditionals were TRUE.
         */

        /*
         * Create a program that calculates the area of a circle
         * Make sure this program does not accept 0 or negative radii
         * Output the area of the circle.
         * Area = pi x r ^ 2
         * pi = 3.14
         */

        double r = 1.0; // <-- User input
        if (r <= 0) {
            System.out.println("Retype radius above 0");
        } else {
            System.out.println(r * r * 3.14);
        }

        // --- Java Switch Statements ---
        // Tax form fillout application
        // Asks the user their filing status:
        // 0: Single 1: Married/Widow 2: Married Separately 3: Head of household
        int status = 0;
        if (status == 0) {
            System.out.println("You're filing single");
        } else if (status == 1) {
            System.out.println("You're filing as married");
        } else if (status == 2) {
            System.out.println("You're filing as married separately");
        } else if (status == 3) {
            System.out.println("You're filing as head of household");
        }

        switch (status) {
            case 0:
                System.out.println("You're filing single");
                break;
            case 1:
                System.out.println("You're filing as married");
                break;
            case 2:
                System.out.println("You're filing as married separately");
                break;
            case 3:
                System.out.println("You're filing as head of household");
                break;
            default:
                System.out.println("Error, please retype status");
                // The breaks prevent "fall-through" error where
                // the code runs all cases including default
        }

        int age2 = 22;
        boolean hasID = true;
        if (age2 >= 18) {
            if (hasID) {
                System.out.println("Entry allowed.");
            } else {
                System.out.println("Old enough, but ID required.");
            }
        } else {
            System.out.println("Not old enough");
        }

        // Equivalent if statement
        if (age2 >= 18 && hasID) {
            System.out.println("Entry allowed.");
        } else if (age2 >= 18 && !hasID) {
            System.out.println("Old enough, but ID required.");
        } else {
            System.out.println("Not old enough");
        }

        boolean loggedIn = false;
        if (loggedIn)
            System.out.println("Welcome Back!");
            System.out.println("This prints when loggedIn is false");

        if (loggedIn) {
            System.out.println("Welcome Back!");
            System.out.println("This prints when loggedIn is false");
        }

        int n = -5;
        if (n > 0); // <- stray semicolon terminates the if immediately
        {
            System.out.println("This print, even if though n is -5");
        }

        // Short circuits: && and ||
        int dividend = 10;
        int divisor = 0;
        // && -> If the left side is false: the right is never evaluated
        // || -> If the left side is true: the right is never evaluated
        // Use only a singular & / | to ensure both sides are evaluated
        if (divisor != 0 && (dividend / divisor == 2)) {
            System.out.println("Runs");
        } else {
            System.out.println("Error: divide by zero.");
        }

        // Floating-point numbers
        double total = 0.1 + 0.2;
        if (total == 0.3) {
            System.out.println("Total == 0.3 exactly");
        } else {
            System.out.println("Total (" + total + ") is not exactly 0.3");
        }
        if (Math.abs(total - 0.3) < 1e-9) {
            System.out.println("Total is close enough.");
        }
            
    }
}
