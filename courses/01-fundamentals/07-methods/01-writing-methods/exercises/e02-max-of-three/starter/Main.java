import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter three numbers: ");
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();

        System.out.println("Max: " + max(a, b, c));
    }

    /** Returns the largest of a, b, and c. */
    public static int max(int a, int b, int c) {
        return 0; // TODO
    }
}
