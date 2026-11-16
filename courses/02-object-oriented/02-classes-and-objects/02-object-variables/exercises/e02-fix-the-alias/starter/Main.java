public class Main {
    public static void main(String[] args) {
        // We want two different robots: Bolt with 100% battery and Volt with 40%.
        Robot bolt = new Robot("Bolt", 100);
        Robot volt = bolt;
        volt.name = "Volt";
        volt.battery = 40;

        System.out.println(bolt.name + " has " + bolt.battery + "% battery");
        System.out.println(volt.name + " has " + volt.battery + "% battery");
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
