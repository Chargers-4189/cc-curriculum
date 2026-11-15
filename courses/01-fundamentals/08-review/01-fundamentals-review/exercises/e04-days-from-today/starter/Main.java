import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter today's day (1 = Monday ... 7 = Sunday): ");
        int day = input.nextInt();
        System.out.print("Enter the number of days: ");
        int length = input.nextInt();

        int dayAfterLength = 0; // TODO: calculate with + - * / %

        System.out.println("In " + length + " days it will be day " + dayAfterLength);
    }
}
