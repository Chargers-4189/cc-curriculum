public class Main {
    public static void main(String[] args) {
        Robot first = new Robot("Bolt", 100);
        Robot second = new Robot("Volt", 40);
        System.out.println("First: " + first.name + ", second: " + second.name);

        // Swap them, so first refers to Volt and second refers to Bolt.
        // Don't make any new robots, and don't change their names.
        Robot temp = first;
        first = second;
        second = temp;

        System.out.println("First: " + first.name + ", second: " + second.name);
    }
}

// The Robot class is done. Don't change it.
class Robot {
    String name;
    int battery;

    Robot(String name, int battery) {
        this.name = name;
        this.battery = battery;
    }
}
