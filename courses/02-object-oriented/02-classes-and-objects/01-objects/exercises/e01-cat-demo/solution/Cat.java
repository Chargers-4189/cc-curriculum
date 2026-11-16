public class Cat {
    // --- What an Object Knows ---
    // Classes are blueprints. We don't know which cat we're making yet,
    // so these don't get values here. Each cat gets its own.
    String name;
    String color;
    String breed;
    double size;

    // --- What an Object Does ---
    void meow() {
        System.out.println("Meow");
    }

    void walk(double pace) {
        System.out.println(name + " is walking at pace " + pace);
    }

    void sleep() {
        System.out.println(name + " is asleep");
    }
}
