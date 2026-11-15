/**
 * Write a program that displays all the leap years, ten per line,
 * from 101 to 2100, separated by exactly one space.
 * Also display the number of leap years in this period.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("Leap Years between 101 and 2100: ");
        int total = 0;
        int lineIdx = 0; // how many years are on the current line
        for (int i = 101; i <= 2100; i++) {
            if ((i % 4 == 0 && i % 100 != 0) || (i % 400 == 0)) {
                if (lineIdx > 0) {
                    System.out.print(" "); // exactly one space between years
                }
                System.out.print(i);
                lineIdx++;
                total++;
                if (lineIdx == 10) {
                    System.out.println();
                    lineIdx = 0;
                }
            }
        }
        if (lineIdx != 0) {
            System.out.println(); // finish the last, partly filled line
        }
        System.out.println("Total leap years is " + total);
    }
}
