import java.util.ArrayList;

public class ListsDemo {
    public static void main(String[] args) {
        // --- Making an ArrayList ---
        ArrayList<String> parts = new ArrayList<>();
        System.out.println(parts.size());          // 0: it starts empty

        // --- Adding and Getting ---
        parts.add("motor");
        parts.add("wheel");
        parts.add("bumper");
        System.out.println(parts);                 // [motor, wheel, bumper]
        System.out.println(parts.get(1));          // wheel
        System.out.println(parts.size());          // 3
        parts.add(1, "battery");                   // squeeze one in at index 1
        System.out.println(parts);                 // [motor, battery, wheel, bumper]

        // --- Changing and Removing ---
        parts.set(0, "falcon motor");
        parts.remove("wheel");                     // remove by value
        parts.remove(0);                           // remove by index
        System.out.println(parts);                 // [battery, bumper]

        // --- Searching ---
        System.out.println(parts.contains("bumper"));   // true
        System.out.println(parts.indexOf("bumper"));    // 1
        System.out.println(parts.indexOf("camera"));    // -1: not there
        System.out.println(parts.isEmpty());            // false

        // --- Looping ---
        for (int i = 0; i < parts.size(); i++) {
            System.out.println(i + ": " + parts.get(i));
        }
        for (String part : parts) {
            System.out.println("- " + part);
        }

        // --- ArrayLists of Objects ---
        ArrayList<Robot> team = new ArrayList<>();
        team.add(new Robot("Bolt", 70));
        team.add(new Robot("Volt", 100));
        for (Robot r : team) {
            System.out.println(r.getName() + ": " + r.getBattery() + "%");
        }

        // --- Primitives Need Wrappers ---
        ArrayList<Integer> scores = new ArrayList<>();   // not ArrayList<int>
        scores.add(85);
        scores.add(92);
        int total = 0;
        for (int s : scores) {
            total += s;
        }
        System.out.println("Total: " + total);
    }
}
