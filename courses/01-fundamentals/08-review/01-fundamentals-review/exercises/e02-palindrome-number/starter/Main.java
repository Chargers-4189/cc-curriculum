import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = input.nextInt();

        System.out.println(number + " reversed is " + reverse(number));
        // Print whether number is a palindrome
    }

    /** Returns the digits of number in reverse order. */
    public static int reverse(int number) {
        return 0; // TODO
    }

    /** Returns true if number reads the same forwards and backwards. */
    public static boolean isPalindrome(int number) {
        return false; // TODO
    }
}
