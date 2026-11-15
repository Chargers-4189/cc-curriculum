import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter seconds: ");
        int seconds = input.nextInt();

        int minutes = seconds / 60;
        int remaining = seconds % 60;

        System.out.println(seconds + " seconds is " + minutes + " minutes and " + remaining + " seconds");
    }
}
