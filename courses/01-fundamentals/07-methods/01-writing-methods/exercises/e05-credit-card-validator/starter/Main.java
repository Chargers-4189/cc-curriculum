import java.util.Scanner;

public class Main {
    /*
        Project - Credit Card Validator

        Implement the Luhn check. A card number is valid if:
        1. Double every second digit from the right. If doubling
            gives two digits, add those two digits together
        2. Sum those results
        3. Sum the digits in the odd positions from the right
        4. Add steps 2 and 3. If the total is divisible by 10,
            card is valid

            4388576018410707 is valid
            4388576018402626 is invalid
    */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

    }

    /** Return true if the card number is valid */
    public static boolean isValid(long number) {
        return false; // TODO
    }

    /** Get the result from Step 2 */
    public static int sumOfDoubleEvenPlace(long number) {
        return 0; // TODO
    }

    /** Return the sum of the odd-place digits in number (Step 3) */
    public static int sumOfOddPlace(long number) {
        return 0; // TODO
    }

    /** Return this number if it is a single digit, otherwise return the sum of the two digits */
    public static int getDigit(int number) {
        return 0; // TODO
    }

    /** Return the number of digits in d */
    public static int getSize(long d) {
        return 0; // TODO
    }

    /** Return the first k digits of number. If number has fewer than k digits, return number. */
    public static long getPrefix(long number, int k) {
        return 0; // TODO
    }

    /** Return true if the number d is a prefix for number */
    public static boolean prefixMatched(long number, int d) {
        // 4=Visa, 5=MC, 37=AmEx, 6=Discover
        return false; // TODO
    }
}
