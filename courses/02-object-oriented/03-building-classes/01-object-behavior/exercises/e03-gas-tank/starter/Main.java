public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.fuel = 10;
        car.mpg = 25;

        car.drive(50);
        System.out.println("Fuel left: " + car.getFuel());
        car.drive(100);
        System.out.println("Fuel left: " + car.getFuel());
        System.out.println("Miles left: " + car.milesLeft());
    }
}

class Car {
    double fuel;   // gallons in the tank
    double mpg;    // miles per gallon

    // drive(double miles): uses up miles / mpg gallons of fuel

    // getFuel(): gives back how much fuel is left

    // milesLeft(): gives back how many miles the car can still go

}
