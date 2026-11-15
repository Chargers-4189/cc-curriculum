public class ForLoops {
    public static void main(String[] args) {
        // --- Same Loop, One Line ---
        for (int k = 0; k < 10; k++) {
            System.out.println("Welcome to Java!");
        }

        // --- Order of Execution ---
        // 1. int k = 0 runs once   2. check k < 3   3. body   4. k++   5. back to 2
        for (int k = 0; k < 3; k++) {
            System.out.println("k is " + k);
        }
        // System.out.println(k); // won't compile: k only exists inside the loop

        // --- Counting Different Ways ---
        for (int k = 5; k >= 1; k--) {
            System.out.print(k + " ");     // 5 4 3 2 1
        }
        System.out.println();

        for (int k = 0; k <= 20; k += 5) {
            System.out.print(k + " ");     // 0 5 10 15 20
        }
        System.out.println();

        // --- Nested For Loops ---
        for (int row = 1; row <= 9; row++) {
            System.out.print(row + " | ");
            for (int col = 1; col <= 9; col++) {
                System.out.printf("%4d", row * col);
            }
            System.out.println();
        }

        // --- break and continue ---
        // break: stop once the sum reaches 100
        int bSum = 0;
        for (int n = 1; n <= 20; n++) {
            bSum += n;
            if (bSum >= 100) {
                break;
            }
        }
        System.out.println("Stopped at sum = " + bSum); // 105

        // continue: add only the odd numbers
        int cSum = 0;
        for (int n = 1; n <= 20; n++) {
            if (n % 2 == 0) {
                continue; // skip the rest of this pass
            }
            cSum += n;
        }
        System.out.println("Sum of odds = " + cSum); // 100
    }
}
