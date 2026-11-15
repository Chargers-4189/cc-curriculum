public class ArraysDemo {
    public static void main(String[] args) {
        // --- Creating an Array ---
        int[] scores = {90, 85, 72, 100, 64};
        String[] names = {"Ada", "Grace", "Alan"};
        double[] temperatures = new double[7];   // 7 slots, all starting at 0.0
        System.out.println(names[0]);            // Ada
        System.out.println(temperatures[3]);     // 0.0

        // --- Indexes ---
        System.out.println(scores[0]);  // 90, the first element
        System.out.println(scores[4]);  // 64, the last element
        scores[2] = 75;                 // change the third element
        System.out.println(scores[2]);  // 75

        // --- Length ---
        System.out.println(scores.length);                // 5
        System.out.println(scores[scores.length - 1]);    // 64, always the last element

        // --- Out of Bounds ---
        // System.out.println(scores[5]); // crashes: ArrayIndexOutOfBoundsException (valid indexes are 0 to 4)

        // --- Looping Through an Array ---
        for (int i = 0; i < scores.length; i++) {
            System.out.println("Score " + i + ": " + scores[i]);
        }

        // Sum and average
        int sum = 0;
        for (int i = 0; i < scores.length; i++) {
            sum += scores[i];
        }
        double average = (double) sum / scores.length;  // cast to avoid integer division
        System.out.println("Average: " + average);      // 82.8

        // Highest value
        int max = scores[0];
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > max) {
                max = scores[i];
            }
        }
        System.out.println("Highest: " + max);          // 100
    }
}
