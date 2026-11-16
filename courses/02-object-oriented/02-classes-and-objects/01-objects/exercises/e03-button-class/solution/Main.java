public class Main {
    public static void main(String[] args) {
        Button back = new Button();
        back.label = "Backspace";
        back.color = "Pink";

        Button launch = new Button();
        launch.label = "Nuclear launch";
        launch.color = "Red";

        back.push();
        back.release();
        launch.push();
        System.out.println("The launch button is " + launch.color);
    }
}

// Write the Button class here.
// A Button knows its label and its color (both Strings).
// A Button can push() and release().
class Button {
    String label;
    String color;

    void push() {
        System.out.println(label + " was pushed");
    }

    void release() {
        System.out.println(label + " was released");
    }
}
