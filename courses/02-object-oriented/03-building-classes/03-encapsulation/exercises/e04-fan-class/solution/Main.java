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
    private int speed;
    private boolean on;
    private double radius;
    private String color;

    public Fan() {
        speed = SLOW;
        on = false;
        radius = 5;
        color = "blue";
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        if (speed >= SLOW && speed <= FAST) {
            this.speed = speed;
        }
    }

    public boolean isOn() {
        return on;
    }

    public void setOn(boolean on) {
        this.on = on;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        if (radius > 0) {
            this.radius = radius;
        }
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String describe() {
        if (on) {
            return "speed " + speed + ", color " + color + ", radius " + radius;
        } else {
            return "color " + color + ", radius " + radius + ", fan is off";
        }
    }
}
