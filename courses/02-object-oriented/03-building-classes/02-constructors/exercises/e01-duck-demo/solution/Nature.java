public class Nature {
    public static void main(String[] args) {
        // --- Making an Object ---
        Duck d;           // 1. declare a reference variable
        d = new Duck();   // 2. make the object (the constructor runs)  3. link them

        // --- Writing a Constructor ---
        System.out.println(d.name + " is size " + d.size);

        // --- Overloaded Constructors ---
        Duck myDuck = new Duck(10, "Quackers");
        Duck bigDuck = new Duck(40);
        System.out.println(myDuck.name + " is size " + myDuck.size);

        // --- Default Values ---
        System.out.println(bigDuck.name);   // null: nobody set it
        bigDuck.setSize(45);
        System.out.println(bigDuck.size);
    }
}
