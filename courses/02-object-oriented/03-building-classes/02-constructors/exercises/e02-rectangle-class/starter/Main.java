public class Main {
    public static void main(String[] args) {
        Rectangle square = new Rectangle();
        Rectangle wide = new Rectangle(4, 40);
        Rectangle small = new Rectangle(3.5, 2);

        System.out.println(square.width + " x " + square.height + ": area " + square.getArea() + ", perimeter " + square.getPerimeter());
        System.out.println(wide.width + " x " + wide.height + ": area " + wide.getArea() + ", perimeter " + wide.getPerimeter());
        System.out.println(small.width + " x " + small.height + ": area " + small.getArea() + ", perimeter " + small.getPerimeter());
    }
}

class Rectangle {
    double width;
    double height;

    // A no-arg constructor: makes a 1 by 1 rectangle

    // A constructor that takes the width and height

    // getArea(): width times height

    // getPerimeter(): all four sides added up

}
