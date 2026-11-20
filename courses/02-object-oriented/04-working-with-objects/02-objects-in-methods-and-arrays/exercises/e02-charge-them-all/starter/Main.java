public class Main {
    public static void main(String[] args) {
        Robot[] team = new Robot[3];
        team[0] = new Robot("Bolt", 40);
        team[1] = new Robot("Volt", 90);
        team[2] = new Robot("Amp", 10);

        printTeam(team);
        chargeAll(team, 25);
        System.out.println("After charging:");
        printTeam(team);
    }

    // printTeam: print each robot as <name>: <battery>%

    // chargeAll: charge every robot in the array by amount
}

// Robot is done. Don't change it.
class Robot {
    private String name;
    private int battery;

    public Robot(String name, int battery) {
        this.name = name;
        this.battery = battery;
    }

    public String getName() {
        return name;
    }

    public int getBattery() {
        return battery;
    }

    public void charge(int amount) {
        battery = Math.min(battery + amount, 100);
    }
}
