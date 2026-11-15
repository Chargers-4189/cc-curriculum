import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a decimal: ");
        double number = input.nextDouble();

        int whole = (int) number;
        System.out.println("Whole part: " + whole);
    }
}
