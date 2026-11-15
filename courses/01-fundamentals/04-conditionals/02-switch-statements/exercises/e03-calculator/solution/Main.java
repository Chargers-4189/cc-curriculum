import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int a = input.nextInt();
        System.out.print("Enter an operator (+ - * / %): ");
        String op = input.next();
        System.out.print("Enter another number: ");
        int b = input.nextInt();

        switch (op) {
            case "+":
                System.out.println(a + " + " + b + " = " + (a + b));
                break;
            case "-":
                System.out.println(a + " - " + b + " = " + (a - b));
                break;
            case "*":
                System.out.println(a + " * " + b + " = " + (a * b));
                break;
            case "/":
                System.out.println(a + " / " + b + " = " + (a / b));
                break;
            case "%":
                System.out.println(a + " % " + b + " = " + (a % b));
                break;
            default:
                System.out.println("Unknown operator");
        }
    }
}
