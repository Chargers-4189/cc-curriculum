import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int number = (int) (Math.random() * 101);
        Scanner input = new Scanner(System.in);

        int guess = -1;
        while (guess != number) {
            // User to guess the number
            System.out.println("Enter your guess: ");
            guess = input.nextInt();

            if (guess > number) {
                System.out.println("Try again, too high");
            } else if (guess < number) {
                System.out.println("Try again, too low");
            }
        }
        // You win!
        System.out.println("You win!");
    }
}
