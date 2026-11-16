public class BehaviorTester {
    public static void main(String[] args) {
        // --- State Affects Behavior ---
        Dog one = new Dog();
        one.size = 70;
        Dog two = new Dog();
        two.size = 8;
        Dog three = new Dog();
        three.size = 35;

        one.bark();    // Wooof! Wooof!
        two.bark();    // Yip! Yip!
        three.bark();  // Ruff! Ruff!

        // --- Sending Things to a Method ---
        Fish myFish = new Fish();
        myFish.diet = "herbivore";
        myFish.weight = 10;
        myFish.eat(3);

        Fish newFish = new Fish();
        newFish.diet = "carnivore";
        newFish.eat(2);

        // --- Getting Things Back ---
        int w = myFish.getWeight();
        System.out.println("My fish weighs " + w);

        // --- More Than One Parameter ---
        myFish.swim(20, 3);

        // --- Getters and Setters ---
        one.setName("Fido");
        System.out.println(one.getName() + " is size " + one.getSize());
    }
}
