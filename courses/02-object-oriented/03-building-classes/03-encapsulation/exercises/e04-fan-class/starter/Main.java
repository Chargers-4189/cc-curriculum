public class Main {
    public static void main(String[] args) {
        Fan first = new Fan();
        first.setSpeed(Fan.FAST);
        first.setRadius(10);
        first.setColor("yellow");
        first.setOn(true);

        Fan second = new Fan();
        second.setSpeed(Fan.MEDIUM);
        second.setSpeed(7);   // not a real speed, so it stays MEDIUM

        System.out.println(first.describe());
        System.out.println(second.describe());
        second.setOn(true);
        System.out.println(second.describe());
        System.out.println("Is the first fan on? " + first.isOn());
    }
}

class Fan {
    // The three speeds. final means they can never change.
    // Use them like Fan.SLOW from outside the class, or just SLOW inside it.
    public static final int SLOW = 1;
    public static final int MEDIUM = 2;
    public static final int FAST = 3;

    // Write the rest of the Fan class here.

}
