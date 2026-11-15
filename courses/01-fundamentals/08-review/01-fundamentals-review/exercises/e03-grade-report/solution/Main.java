import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("How many students? ");
        int count = input.nextInt();
        System.out.print("Enter the scores: ");

        int[] scores = new int[count];
        for (int i = 0; i < scores.length; i++) {
            scores[i] = input.nextInt();
        }

        int sum = 0;
        int highest = scores[0];
        for (int i = 0; i < scores.length; i++) {
            System.out.println("Student " + (i + 1) + ": " + scores[i] + " (" + letterGrade(scores[i]) + ")");
            sum += scores[i];
            if (scores[i] > highest) {
                highest = scores[i];
            }
        }
        System.out.println("Average: " + (double) sum / scores.length);
        System.out.println("Highest: " + highest);
    }

    /** Returns the letter grade for a score. */
    public static char letterGrade(int score) {
        if (score >= 90) {
            return 'A';
        } else if (score >= 80) {
            return 'B';
        } else if (score >= 70) {
            return 'C';
        } else if (score >= 60) {
            return 'D';
        }
        return 'F';
    }
}
