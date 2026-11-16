public class Dog {
    // --- State Affects Behavior ---
    int size;
    String name;

    void bark() {
        if (size > 60) {
            System.out.println("Wooof! Wooof!");
        } else if (size > 14) {
            System.out.println("Ruff! Ruff!");
        } else {
            System.out.println("Yip! Yip!");
        }
    }

    // --- Getters and Setters ---
    String getName() {
        return name;
    }

    void setName(String newName) {
        name = newName;
    }

    int getSize() {
        return size;
    }

    void setSize(int newSize) {
        size = newSize;
    }
}
