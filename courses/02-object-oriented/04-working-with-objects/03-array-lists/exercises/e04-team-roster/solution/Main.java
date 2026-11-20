import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static final int MAX_TEAM_SIZE = 4;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> team = new ArrayList<>();

        // Read commands until quit: add <name>, remove <name>, list, count
        String command = input.next();
        while (!command.equals("quit")) {
            if (command.equals("add")) {
                String name = input.next();
                if (team.contains(name)) {
                    System.out.println(name + " is already on the team");
                } else if (team.size() >= MAX_TEAM_SIZE) {
                    System.out.println("The team is full");
                } else {
                    team.add(name);
                    System.out.println("Added " + name);
                }
            } else if (command.equals("remove")) {
                String name = input.next();
                if (team.remove(name)) {
                    System.out.println("Removed " + name);
                } else {
                    System.out.println(name + " isn't on the team");
                }
            } else if (command.equals("list")) {
                System.out.println("Team: " + team);
            } else if (command.equals("count")) {
                System.out.println(team.size() + " of " + MAX_TEAM_SIZE);
            } else {
                System.out.println("Unknown command: " + command);
            }
            command = input.next();
        }
        System.out.println("Bye!");
    }
}
