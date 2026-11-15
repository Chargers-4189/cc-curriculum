public class Methods {
    public static void main(String[] args) {
        // --- Why Methods? ---
        System.out.println(sumOfRange(1, 10));   // 55
        System.out.println(sumOfRange(20, 37));  // 513
        System.out.println(sumOfRange(55, 101)); // 3666

        // --- Anatomy of a Method ---
        System.out.println(max(5, 2));           // 5

        // --- void vs Value-Returning ---
        printGrade(90.2);                        // a void method goes on its own line
        System.out.println(getGrade(99.3));      // a returned value can go anywhere a value fits
        double stored = getGrade(87.5) + 2;      // stored, used in math...
        System.out.println(stored);
        // double grade = printGrade(20.3);      // won't compile: printGrade gives nothing back

        // --- Pass-by-Value ---
        int x = 1;
        System.out.println("Before: " + x);
        increment(x);
        System.out.println("After: " + x);       // still 1: increment got a copy

        int num1 = 1;
        int num2 = 2;
        swap(num1, num2);
        System.out.println("After: " + num1 + " " + num2); // After: 1 2

        // --- Scope ---
        for (int n = 0; n < 3; n++) {
            int doubled = n * 2;
            System.out.println(doubled);
        }
        // System.out.println(n);       // won't compile: n only existed in the loop
        // System.out.println(doubled); // same

        // --- Further ---
        System.out.println(max(1.5, 2.5));       // 2.5, Java picks the double version
        System.out.println(max(3.0, 9.0, 4.0));  // 9.0
    }

    // Why Methods?: write the loop once, call it as many times as you want
    public static int sumOfRange(int min, int max) {
        int sum = 0;
        for (int i = min; i <= max; i++) {
            sum += i;
        }
        return sum;
    }

    // Anatomy of a Method: modifiers, return type, name, parameters
    public static int max(int num1, int num2) {
        if (num1 > num2) {
            return num1;
        } else {
            return num2;
        }
    }

    // void vs Value-Returning
    public static void printGrade(double grade) {
        System.out.println(grade);
    }

    public static double getGrade(double grade) {
        return grade;
    }

    // Pass-by-Value: n, n1, and n2 are copies
    public static void increment(int n) {
        n++;
        System.out.println("n inside the method is " + n);
    }

    public static void swap(int n1, int n2) {
        int temp = n1;
        n1 = n2;
        n2 = temp;
        System.out.println("  inside swap: n1 = " + n1 + ", n2 = " + n2);
    }

    // Further: overloading, same name with different parameters
    public static double max(double num1, double num2) {
        if (num1 > num2) {
            return num1;
        }
        return num2;
    }

    public static double max(double num1, double num2, double num3) {
        return max(max(num1, num2), num3); // methods calling methods
    }
}
