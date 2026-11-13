import java.util.Scanner;

public class Validate {
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
        System.out.print("Enter a credit card number as a long integer: ");
        long number = input.nextLong();

        if (isValid(number)) {
            System.out.println(number + " is valid");
        } else {
            System.out.println(number + " is invalid");
        }
    }

    /** Return true if the card number is valid */
    public static boolean isValid(long number) {
        int size = getSize(number);
        boolean rightSize = size >= 13 && size <= 16;
        boolean rightPrefix = prefixMatched(number, 4) || prefixMatched(number, 5)
                || prefixMatched(number, 37) || prefixMatched(number, 6);
        boolean passesLuhn = (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0;
        return rightSize && rightPrefix && passesLuhn;
    }

    /** Get the result from Step 2 */
    public static int sumOfDoubleEvenPlace(long number) {
        int sum = 0;
        number /= 10; // skip the rightmost digit: it's in an odd place
        while (number > 0) {
            int digit = (int) (number % 10);
            sum += getDigit(digit * 2);
            number /= 100; // jump two places to the next even place
        }
        return sum;
    }

    /** Return the sum of the odd-place digits in number (Step 3) */
    public static int sumOfOddPlace(long number) {
        int sum = 0;
        while (number > 0) {
            sum += (int) (number % 10);
            number /= 100;
        }
        return sum;
    }

    /** Return this number if it is a single digit, otherwise return the sum of the two digits */
    public static int getDigit(int number) {
        if (number < 10) {
            return number;
        }
        return number / 10 + number % 10;
    }

    /** Return the number of digits in d */
    public static int getSize(long d) {
        int size = 1;
        while (d >= 10) {
            d /= 10;
            size++;
        }
        return size;
    }

    /** Return the first k digits of number. If number has fewer than k digits, return number. */
    public static long getPrefix(long number, int k) {
        int extraDigits = getSize(number) - k;
        for (int i = 0; i < extraDigits; i++) {
            number /= 10;
        }
        return number;
    }

    /** Return true if the number d is a prefix for number */
    public static boolean prefixMatched(long number, int d) {
        // 4=Visa, 5=MC, 37=AmEx, 6=Discover
        return getPrefix(number, getSize(d)) == d;
    }
}
