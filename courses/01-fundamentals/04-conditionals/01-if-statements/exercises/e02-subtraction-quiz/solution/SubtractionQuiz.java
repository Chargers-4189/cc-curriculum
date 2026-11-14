import java.util.Scanner;

public class SubtractionQuiz {
    public static void main(String[] args) {
        // 1. Generate two single-digit numbers
        int num1 = (int) (Math.random() * 10);
        int num2 = (int) (Math.random() * 10);

        // 2. Make sure num1 is not smaller than num2; if it is, swap
        if (num1 < num2) {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }

        // 3. Prompt the student
        Scanner input = new Scanner(System.in);
        System.out.print("What is " + num1 + " - " + num2 + "? ");
        int answer = input.nextInt();

        // 4. Check their answer
        if (num1 - num2 == answer) {
            System.out.println("You are correct!");
        } else {
            System.out.println("Your answer is wrong.");
            System.out.println(num1 + " - " + num2 + " is " + (num1 - num2));
        }
    }
}
