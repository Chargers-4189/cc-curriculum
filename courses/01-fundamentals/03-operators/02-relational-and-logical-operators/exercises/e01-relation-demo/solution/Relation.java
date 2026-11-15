public class Relation {
    public static void main(String[] args) {
        // --- Relational Operators ---
        int a = 10;
        int b = 20;
        System.out.println("a < b: " + (a < b));   // true
        System.out.println("a > b: " + (a > b));   // false
        System.out.println("a <= b: " + (a <= b)); // true
        System.out.println("a >= b: " + (a >= b)); // false
        System.out.println("a == b: " + (a == b)); // false
        System.out.println("a != b: " + (a != b)); // true

        // = assigns, == compares. One = by mistake changes a to 20!
        // System.out.println("a == b: " + (a = b));

        // --- Comparing Different Types ---
        System.out.println(10 == 10.0); // true: 10 becomes 10.0 first

        // --- Comparing Decimals ---
        System.out.println(0.1 + 0.2);          // 0.30000000000000004
        System.out.println((0.1 + 0.2) == 0.3); // false!

        double c = 0.1 + 0.2;
        double d = 0.3;
        double THRESHOLD = 1e-9;                         // 0.000000001
        System.out.println(Math.abs(c - d) < THRESHOLD); // true: close enough to equal

        // --- Comparing Strings ---
        String answer = "yes";
        System.out.println(answer.equals("yes")); // true

        // --- Logical Operators ---
        int x = 10;
        System.out.println(x > 0 && x < 50); // true:  both sides are true
        System.out.println(x > 0 || x < 5);  // true:  the left side is true
        System.out.println(!true);           // false: ! flips it

        // --- Short-Circuit Evaluation ---
        int u = 10, r = 15;
        System.out.println(u < r || 0 == 1 / 0); // true:  the right side never runs
        System.out.println(u > r && 0 == 1 / 0); // false: the right side never runs
        // System.out.println(u < r | 0 == 1 / 0); // crashes: | always runs both sides

        // --- Operator Precedence ---
        System.out.println(2 * 3 + 1);      // 7
        System.out.println(2 * (3 + 1));    // 8
        System.out.println(x > 0 && x < 10); // false: comparisons first, then &&

        int age = 17;
        System.out.println("age is between 16 and 21: " + (age > 16 && age < 21)); // true
    }
}
