import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the dividend: ");
        int dividend = input.nextInt();
        System.out.print("Enter the divisor: ");
        int divisor = input.nextInt();

        if (divisor != 0) {
            System.out.println(dividend + " / " + divisor + " = " + (dividend / divisor));
        } else {
            System.out.println("Cannot divide by zero");
        }
    }
}
