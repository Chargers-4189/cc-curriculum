import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter start, end, and step: ");
        int start = input.nextInt();
        int end = input.nextInt();
        int step = input.nextInt();

        printTable(start, end, step);
    }

    /** Prints one row per step: the Fahrenheit temperature and its Celsius value. */
    public static void printTable(int startF, int endF, int step) {
        for (int f = startF; f <= endF; f += step) {
            int c = 5 / 9 * (f - 32); // the bug is in this line
            System.out.println(f + " " + c);
        }
    }
}
