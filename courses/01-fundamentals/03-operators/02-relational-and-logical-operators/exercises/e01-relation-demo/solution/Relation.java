public class Relation {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        System.out.println("a < b: " + (a < b)); // True <- 10 < 20
        System.out.println("a > b: " + (a > b)); // False <- 10 > 20 
        System.out.println("a <= b: " + (a <= b)); // True <- 10 <= 20
        System.out.println("a >= b: " + (a >= b)); // False <- 10 >= 20
        System.out.println("a == b: " + (a == b)); // False <- 10 == 20
        System.out.println("a != b: " + (a != b)); // True <- 10 != 20

        // Be careful about the amount of = you use.
        // = Is for assigning values
        // == Is for comparing values
        //System.out.println("a == b: " + (a = b)); // Using one: = instead of two: ==

        // Comparing mixed datatypes: int & doubles
        // int will be converted to a double before comparison
        System.out.println("10 == 10.0 " + (10 == 10.0)); // True (Converts 10 -> 10.0)

        System.out.println(0.1 + 0.2); // 0.3 (real world) 0.30000000000000004 by computer
        System.out.println((0.1 + 0.2) == 0.3); // False 0.30000000000000004 != 0.3

        // --- Comparing floating-point numbers ---
        double c = (0.1 + 0.2);
        double d = 0.3;
        double THRESHOLD = 1e-9;
        // 0.000000001
        // 0.30000000000000004
        System.out.println(Math.abs(c - d) < THRESHOLD); // TRUE (Math.abs: the difference could be negative)
        // If we're comparing 4.1 and 4.2 to see if equal
        // • 4.1 - 4.2 = -0.1 (Close but not equal)
        // • 4.1 - 4.1 = 0 (Since 0, then they are equal)

        // Above is calculating if the difference between
        // the values is close to 0 -> equal to each other

        // --- String comparisons (Technically object comparisons) ---
        String s1 = new String("Hello");
        String s2 = new String("Hello");
        // == Comparing objects will check if they point to the same thing in memory
        // obj1 => memorySlot2
        // obj2 -> memorySlot2
        // obj1 == obj2 -> True

        // obj3 => memorySlot2
        // obj4 -> memorySlot1
        // obj3 == obj4 -> False
        System.out.println("Comparing s1 and s2: " + (s1 == s2));
        System.out.println("Comparing s1 and s2 using .equals: " + (s1.equals(s2)));

        // --- Logical Operators ---
        // AND: && is only true if both sides are TRUE
        // OR: || is true if AT LEAST one side is TRUE
        // NOT: ! Flips a boolean
        // XOR: ^ Exclusive or; is true only when both sides DIFFER.

        // 40 != 53
        // 50 > 0 ^ 40 < 0 == false

        int u = 10;
        int r = 15;
        System.out.println( u > 0 && u < 50); // 0 < 10 < 50 == TRUE
        System.out.println( u > 0 || u < 5); // T OR F == TRUE
        System.out.println( !true ); // false

        // Short-circuit evaluation:
        // && and || is lazy, they skip evaluting right side if
        // result is determined by left side alone.

        // These do not hit the / 0 error since short-circuit
        // evals skip them.
        System.out.println(u < r || 0 == 1/0);
        System.out.println(u > r && 0 == 1/0);

        // Non-short circuit logical operators: & |
        // ALWAYS evaluates both sides
        //System.out.println(u < r | 0 == 1/0); // Forces right side to evaluate
        //System.out.println(u > r & 0 == 1/0); // Forces right side to evaluate

        String str = null;
        //System.out.println(str.length()); Crashes because str is null
        if (str != null && str.length() > 0) { // Need to use double && to prevent both side eval
            System.out.println("Null example: " + str.equals(s1));
        }

        //int age = 0;
        //System.out.println(/* TYPE HERE: print True if age is above 16 and below 21; print false otherwise */);

        int age = 17;
        System.out.println("age is between 16 and 21: " + (age > 16 && age < 21));
    }
}
