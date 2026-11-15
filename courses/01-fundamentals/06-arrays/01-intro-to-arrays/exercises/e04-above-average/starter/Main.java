import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("How many scores? ");
        int count = input.nextInt();
        System.out.print("Enter the scores: ");

        int[] scores = new int[count];
        for (int i = 0; i < scores.length; i++) {
            scores[i] = input.nextInt();
        }

        // Loop 1: find the average

        // Loop 2: count the scores above it
    }
}
