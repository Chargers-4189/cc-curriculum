// Robot is done for you. Don't change it.
public class Robot {
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
