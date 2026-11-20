import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter items, then done:");

        // 1. Read items (one per line) into an ArrayList<String> until the user types done
        ArrayList<String> items = new ArrayList<>();
        String item = input.nextLine();
        while (!item.equals("done")) {
            items.add(item);
            item = input.nextLine();
        }

        // 2. Print how many items there are, then each one numbered from 1
        System.out.println("You have " + items.size() + " items:");
        for (int i = 0; i < items.size(); i++) {
            System.out.println((i + 1) + ". " + items.get(i));
        }
    }
}
