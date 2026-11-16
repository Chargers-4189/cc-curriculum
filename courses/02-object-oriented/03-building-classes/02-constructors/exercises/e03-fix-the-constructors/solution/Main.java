public class Main {
    public static void main(String[] args) {
        Pet stray = new Pet();
        Pet dog = new Pet("Biscuit", 3);

        stray.describe();
        dog.describe();
    }
}

class Pet {
    String name;
    int age;

    public Pet() {
        name = "Unknown";
        age = 0;
    }

    public Pet(String newName, int newAge) {
        name = newName;
        age = newAge;
    }

    void describe() {
        System.out.println(name + " is " + age + " years old");
    }
}
