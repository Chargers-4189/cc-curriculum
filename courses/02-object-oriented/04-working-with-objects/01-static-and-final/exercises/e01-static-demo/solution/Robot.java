public class Robot {
    // --- Static Variables ---
    // One copy for the whole class, shared by every robot
    private static int robotCount = 0;

    // --- Constants ---
    // public is fine here: nobody can change it anyway
    public static final int MAX_BATTERY = 100;

    // --- final Variables ---
    // Set once in the constructor, then it can never change
    private final String name;
    private int battery;

    public Robot(String name) {
        this.name = name;
        battery = MAX_BATTERY;
        robotCount++;
    }

    public static int getRobotCount() {
        return robotCount;
    }

    public String getName() {
        return name;
    }

    public int getBattery() {
        return battery;
    }
}
