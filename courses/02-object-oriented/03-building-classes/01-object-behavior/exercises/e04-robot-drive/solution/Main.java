public class Main {
    public static void main(String[] args) {
        Robot bot = new Robot();
        bot.name = "Bolt";
        bot.battery = 50;

        bot.drive(10);
        bot.drive(20);
        bot.drive(15);
        System.out.println("Battery: " + bot.getBattery() + "%");
        System.out.println("Distance: " + bot.getDistance() + " meters");

        bot.charge(80);
        System.out.println("Battery: " + bot.getBattery() + "%");
        bot.drive(15);
        System.out.println("Distance: " + bot.getDistance() + " meters");
    }
}

class Robot {
    String name;
    int battery;    // 0 to 100
    int distance;   // meters driven so far

    // Write drive, charge, getBattery and getDistance here.
    void drive(int meters) {
        int cost = meters * 2;
        if (cost > battery) {
            System.out.println(name + " doesn't have enough battery to drive " + meters + " meters");
        } else {
            battery = battery - cost;
            distance = distance + meters;
            System.out.println(name + " drove " + meters + " meters");
        }
    }

    void charge(int amount) {
        battery = battery + amount;
        if (battery > 100) {
            battery = 100;
        }
    }

    int getBattery() {
        return battery;
    }

    int getDistance() {
        return distance;
    }
}
