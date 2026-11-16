public class Main {
    public static void main(String[] args) {
        // 1. Make a Cat named Luna and make her walk at pace 1.5
        Cat luna = new Cat();
        luna.name = "Luna";
        luna.walk(1.5);

        // 2. Make a second Cat named Biscuit and make him meow
        Cat biscuit = new Cat();
        biscuit.name = "Biscuit";
        biscuit.meow();

        // 3. Make Luna meow
        luna.meow();
    }
}

// The Cat class is done. Don't change it.
class Cat {
    String name;
    String color;

    void meow() {
        System.out.println(name + " says meow");
    }

    void walk(double pace) {
        System.out.println(name + " is walking at pace " + pace);
    }
}
