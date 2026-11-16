public class Fish {
    int weight;
    String diet;   // "herbivore" or "carnivore"

    // --- Sending Things to a Method ---
    // numOfBites is a parameter: a local variable that gets its value from the caller
    void eat(int numOfBites) {
        while (numOfBites > 0) {
            if (diet.equals("herbivore")) {
                System.out.println("Eating plants...");
            } else if (diet.equals("carnivore")) {
                System.out.println("Eating other fish...");
            } else {
                System.out.println("Don't know my diet.");
            }
            numOfBites--;
        }
    }

    // --- Getting Things Back ---
    int getWeight() {
        return weight;
    }

    // --- More Than One Parameter ---
    void swim(int distance, int speed) {
        System.out.println("Swimming " + distance + " meters at speed " + speed);
    }
}
