import java.util.Scanner;

public class NumberPyramid {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of lines: ");
        int lines = input.nextInt();

        if (lines < 1 || lines > 15) {
            System.out.println("The number of lines must be from 1 to 15");
            return;
        }

        for (int row = 1; row <= lines; row++) {
            // 1. leading spaces: 3 for every number missing on the left
            for (int space = 0; space < lines - row; space++) {
                System.out.print("   ");
            }
            // 2. descending half
            for (int num = row; num >= 1; num--) {
                System.out.printf("%3d", num);
            }
            // 3. ascending half
            for (int num = 2; num <= row; num++) {
                System.out.printf("%3d", num);
            }
            System.out.println();
        }
    }
}
