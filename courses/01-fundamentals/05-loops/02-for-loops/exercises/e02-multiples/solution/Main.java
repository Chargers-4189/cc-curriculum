import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = input.nextInt();

        for (int k = 1; k <= 5; k++) {
            System.out.print(number * k + " ");
        }
        System.out.println();
    }
}
