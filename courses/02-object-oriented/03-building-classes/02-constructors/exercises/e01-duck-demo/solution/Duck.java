public class Duck {
    String name;
    int size;

    // --- Writing a Constructor ---
    // Same name as the class, no return type (not even void)
    public Duck() {
        System.out.println("Quack");
        size = 2;
        name = "Dandelion";
    }

    // --- Overloaded Constructors ---
    public Duck(int newSize) {
        size = newSize;
    }

    public Duck(int newSize, String newName) {
        size = newSize;
        name = newName;
    }

    // --- this ---
    public void setSize(int size) {
        this.size = size;   // this.size is the instance variable, size is the parameter
    }
}
