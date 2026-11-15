import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a score (-1 to stop): ");
        int score = input.nextInt();

        int count = 0;
        int total = 0;
        while (score != -1) {
            total += score;
            count++;
            System.out.print("Enter a score (-1 to stop): ");
            score = input.nextInt();
        }

        if (count == 0) {
            System.out.println("No scores entered");
        } else {
            System.out.println("Count: " + count);
            System.out.println("Average: " + (double) total / count);
        }
    }
}
