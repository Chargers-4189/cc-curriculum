public class ArraysDemo {
    public static void main(String[] args) {
        int[] scores = {90, 85, 72, 100, 64};

        // Accessing elements: indexes start at 0
        System.out.println("First: " + scores[0]);                 // 90
        System.out.println("Last: " + scores[scores.length - 1]);  // 64
        System.out.println("Count: " + scores.length);             // 5

        // Changing an element
        scores[2] = 75;
        System.out.println("Third is now: " + scores[2]);          // 75

        // Looping through every element
        for (int i = 0; i < scores.length; i++) {
            System.out.println("Score " + i + ": " + scores[i]);
        }

        // Average
        int sum = 0;
        for (int i = 0; i < scores.length; i++) {
            sum += scores[i];
        }
        double average = (double) sum / scores.length;             // cast to avoid integer division
        System.out.println("Average: " + average);                 // 82.8

        // Highest
        int max = scores[0];
        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > max) {
                max = scores[i];
            }
        }
        System.out.println("Highest: " + max);                     // 100

        // System.out.println(scores[5]); // ArrayIndexOutOfBoundsException: valid indexes are 0 to 4
    }
}
