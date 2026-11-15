import java.util.Scanner; // for Scanner (imports always go at the very top of the file)

public class Variables {
    public static void main(String[] args) {
        // --- Variables ---
        String firstName;       // declaration: the variable exists, but holds nothing yet
        firstName = "Steve";    // initialization: now it holds a value
        System.out.println(firstName);

        // --- Declaration & Initialization ---
        int age = 16;           // both at once, which is what you'll normally do
        double price = 19.99;
        char grade = 'A';       // single quotes = char, double quotes = String
        boolean isJavaFun = false;
        System.out.println(age + " " + price + " " + grade + " " + isJavaFun);

        age = 17;               // a new value, but age is still an int
        System.out.println(age);
        // age = "seventeen";   // won't compile: age can only ever hold an int

        // --- Data Types ---
        int biggest = 2147483647;  // the biggest value an int can hold
        String greeting = "Hello World";
        System.out.println(biggest);
        System.out.println(greeting);

        // --- Type Casting ---
        int myInt = 12;
        double myDouble = myInt;         // widening: Java does it for you
        System.out.println(myDouble);    // 12.0

        double myDecimal = 12.5;
        int myWhole = (int) myDecimal;   // narrowing: you have to cast
        System.out.println(myWhole);     // 12, the decimal is cut off, not rounded

        // --- Getting Input from the User ---
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = input.nextLine();  // reads a whole line of text

        System.out.print("Enter your age: ");
        int yourAge = input.nextInt();   // reads an int (age is already taken!)

        System.out.println("Hi " + name + ", you are " + yourAge);
    }
}
