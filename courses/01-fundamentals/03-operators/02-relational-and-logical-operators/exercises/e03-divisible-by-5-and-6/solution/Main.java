import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = input.nextInt();

        boolean byFive = number % 5 == 0;
        boolean bySix = number % 6 == 0;

        System.out.println("Divisible by 5 and 6: " + (byFive && bySix));
        System.out.println("Divisible by 5 or 6: " + (byFive || bySix));
        System.out.println("Divisible by 5 or 6, but not both: " + ((byFive || bySix) && !(byFive && bySix)));
    }
}
