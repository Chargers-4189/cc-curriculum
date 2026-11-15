import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number between 0 and 999: ");
        int number = input.nextInt();

        int ones = number % 10;
        int tens = number / 10 % 10;
        int hundreds = number / 100;

        System.out.println("The sum of the digits is " + (ones + tens + hundreds));
    }
}
