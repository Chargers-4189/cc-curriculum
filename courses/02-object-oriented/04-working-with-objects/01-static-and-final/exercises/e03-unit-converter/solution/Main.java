public class Main {
    public static void main(String[] args) {
        System.out.printf("10 feet is %.2f meters%n", Convert.feetToMeters(10));
        System.out.printf("2 meters is %.2f feet%n", Convert.metersToFeet(2));
        System.out.printf("120 pounds is %.2f kilograms%n", Convert.poundsToKilograms(120));
        System.out.println("One foot is " + Convert.METERS_PER_FOOT + " meters");
    }
}

class Convert {
    // Two constants:
    //   METERS_PER_FOOT is 0.3048
    //   KILOGRAMS_PER_POUND is 0.45359237
    public static final double METERS_PER_FOOT = 0.3048;
    public static final double KILOGRAMS_PER_POUND = 0.45359237;

    // feetToMeters, metersToFeet and poundsToKilograms go here
    public static double feetToMeters(double feet) {
        return feet * METERS_PER_FOOT;
    }

    public static double metersToFeet(double meters) {
        return meters / METERS_PER_FOOT;
    }

    public static double poundsToKilograms(double pounds) {
        return pounds * KILOGRAMS_PER_POUND;
    }
}
