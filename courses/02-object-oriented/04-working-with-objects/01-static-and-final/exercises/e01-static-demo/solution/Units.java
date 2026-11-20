public class Units {
    // --- Static Methods ---
    // None of these use instance variables, so they're static
    public static final double METERS_PER_INCH = 0.0254;

    public static double inchesToMeters(double inches) {
        return inches * METERS_PER_INCH;
    }

    public static double metersToInches(double meters) {
        return meters / METERS_PER_INCH;
    }
}
