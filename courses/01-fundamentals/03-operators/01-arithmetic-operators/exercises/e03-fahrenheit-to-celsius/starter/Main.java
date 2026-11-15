import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter degrees Fahrenheit: ");
        double fahrenheit = input.nextDouble();

        double celsius = (5 / 9) * (fahrenheit - 32); // Something is wrong here

        System.out.println("Celsius: " + celsius);
    }
}
