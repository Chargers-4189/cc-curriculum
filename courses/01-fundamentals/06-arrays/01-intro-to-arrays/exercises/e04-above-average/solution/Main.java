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

        int sum = 0;
        for (int i = 0; i < scores.length; i++) {
            sum += scores[i];
        }
        double average = (double) sum / scores.length;

        int above = 0;
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] > average) {
                above++;
            }
        }
        System.out.println("Average: " + average);
        System.out.println("Above average: " + above);
    }
}
