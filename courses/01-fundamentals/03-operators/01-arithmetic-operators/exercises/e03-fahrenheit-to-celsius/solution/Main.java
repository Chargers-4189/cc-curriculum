import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter degrees Fahrenheit: ");
        double fahrenheit = input.nextDouble();

        double celsius = (5.0 / 9) * (fahrenheit - 32);

        System.out.println("Celsius: " + celsius);
    }
}
