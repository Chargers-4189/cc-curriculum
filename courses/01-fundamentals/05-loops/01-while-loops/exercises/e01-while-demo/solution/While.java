import java.util.Scanner;

public class While {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // --- Why Loops? ---
        int count = 0;
        while (count < 100) {
            System.out.println("Welcome to Java!");
            count++;
        }

        // --- The while Loop ---
        int sum = 0, i = 1;
        while (i < 10) {
            sum += i;
            i++;
        }
        System.out.println(sum); // 45

        // --- The Two Things Every Loop Needs ---
        // 1. Something inside the body that changes   (i++)
        // 2. A condition that eventually becomes false (i < 10)
        // Without i++, i stays 1 forever: an infinite loop. Stop it with Ctrl + C.

        // --- Sentinel-Controlled Loops ---
        System.out.print("Enter an integer (ends if it is 0): ");
        int data = input.nextInt();

        int total = 0;
        while (data != 0) {
            total += data;
            System.out.print("Enter an integer (ends if it is 0): ");
            data = input.nextInt();
        }
        System.out.println("Sum is " + total);

        // --- Further ---
        // do-while: the body always runs at least once
        int value;
        int doTotal = 0;
        do {
            System.out.print("Enter an integer (ends if it is 0): ");
            value = input.nextInt();
            doTotal += value;
        } while (value != 0);
        System.out.println("Sum is " + doTotal);
    }
}
