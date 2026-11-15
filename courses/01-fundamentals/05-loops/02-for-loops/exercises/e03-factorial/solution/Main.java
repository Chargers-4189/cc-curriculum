import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter n (0-20): ");
        int n = input.nextInt();

        long factorial = 1;
        for (int k = 2; k <= n; k++) {
            factorial *= k;
        }
        System.out.println(n + "! = " + factorial);
    }
}
