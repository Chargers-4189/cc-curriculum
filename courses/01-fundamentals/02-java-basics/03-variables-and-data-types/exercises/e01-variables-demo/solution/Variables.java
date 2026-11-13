public class Variables {
    public static void main(String[] args) {
        // Declaration or Initialization?
        String firstName;    // Declaration - the variable exists, but holds nothing yet
        firstName = "steve"; // Initialization - now it holds a value
        System.out.println(firstName);

        int myNum = 20;      // Declaration & initialization in one line

        double ratio = 0.5;
        char grade = 'A';    // single quotes = char, double quotes = String
        boolean ready = true;
        System.out.println(myNum + " " + ratio + " " + grade + " " + ready);

        // Narrowing cast: double -> int drops everything after the decimal
        double price = 19.99;
        int wholeDollars = (int) price;
        System.out.println(wholeDollars); // 19
    }
}
