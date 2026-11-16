public class Main {
    public static void main(String[] args) {
        Light lamp = new Light();
        lamp.brightness = 80;
        lamp.describe();
        lamp.toggle();
        lamp.describe();
        lamp.toggle();
        lamp.describe();
    }
}

class Light {
    boolean on;      // starts as false (off)
    int brightness;

    // toggle(): turns the light on if it's off, and off if it's on

    // describe(): prints "Light is on at <brightness>%" or "Light is off"

}
