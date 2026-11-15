import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first word: ");
        String first = input.next();
        System.out.print("Enter the second word: ");
        String second = input.next();

        System.out.println("Same word: " + first.equals(second));
    }
}
