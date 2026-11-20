public class StaticTester {
    public static void main(String[] args) {
        // --- Methods That Don't Need an Object ---
        long rounded = Math.round(42.2);
        int smaller = Math.min(56, 12);
        int distance = Math.abs(-343);
        System.out.println(rounded + " " + smaller + " " + distance);
        // Math m = new Math();   // won't compile: Math's constructor is private

        // --- Static Methods ---
        System.out.println(Units.inchesToMeters(100));   // call it with the class name

        // --- Static Can't Use Instance Variables ---
        // In Robot: a static method that prints name won't compile. Whose name?

        // --- Static Variables ---
        System.out.println(Robot.getRobotCount());   // 0, no robots yet
        Robot a = new Robot("Bolt");
        Robot b = new Robot("Volt");
        Robot c = new Robot("Amp");
        System.out.println(Robot.getRobotCount());   // 3

        // --- Constants ---
        System.out.println(Robot.MAX_BATTERY);
        // Robot.MAX_BATTERY = 200;   // won't compile: it's final

        // --- final Variables ---
        System.out.println(a.getName() + " has " + a.getBattery() + "%");
        // In Robot: name = "Sparky"; inside a method won't compile: name is final
    }
}
