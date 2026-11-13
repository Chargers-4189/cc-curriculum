public class Review {
    public static void main(String[] args) {
        // 1. If today is Friday, what day of the week will it be in 50 days?
        // Use Java arithmetic operators to calculate a day (+ - * / %).
        // Hint: Start with the days of the week numbered 1 -> 7, where 1 is Monday and 7 is Sunday.
        int day = 5;
        int length = 50;
        // Shift to 0-6 so % 7 wraps correctly, then shift back to 1-7
        int dayAfterLength = (day - 1 + length) % 7 + 1;
        System.out.println("Day " + dayAfterLength); // 6 = Saturday

        // 2. Roots of a quadratic: x = (-b +/- sqrt(b^2 - 4ac)) / 2a
        double a = 4;
        double b = -8;
        double c = 1;
        double discriminant = b * b - 4 * a * c;
        if (discriminant < 0) {
            System.out.println("No real roots");
        } else {
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.println("Roots: " + root1 + " and " + root2); // about 1.866 and 0.134
        }
    }
}
