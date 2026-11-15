public class Switch {
    public static void main(String[] args) {
        // --- The Problem ---
        // Filing status: 0 Single, 1 Married / Widow, 2 Married filing separately, 3 Head of household
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

        // --- The switch Statement ---
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
        }

        // --- Fall-Through ---
        // No breaks: everything below the matching case runs too
        int married = 1;
        switch (married) {
            case 0:
                System.out.println("Single");
            case 1:
                System.out.println("Married");
            case 2:
                System.out.println("Married separately");
            default:
                System.out.println("Error");
        }

        // Fall-through on purpose: cases that share code
        int day = 7;
        switch (day) {
            case 1:
            case 7:
                System.out.println("Weekend");
                break;
            default:
                System.out.println("Weekday");
        }

        // --- Further ---
        // Java 14+ arrow form: never falls through, so no break needed
        switch (status) {
            case 0 -> System.out.println("You're filing single");
            case 1 -> System.out.println("You're filing as married");
            default -> System.out.println("Error, please retype status");
        }
    }
}
