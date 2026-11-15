public class Arithmetic {
    public static void main(String[] args) {
        // --- Basic Mathematical Operators ---
        int a = 17, b = 5;
        System.out.println(a + b); // 22
        System.out.println(a - b); // 12
        System.out.println(a * b); // 85
        System.out.println(a / b); // 3
        System.out.println(a % b); // 2

        // --- Modulus ---
        // % gives the remainder: 17 / 5 is 3 with 2 left over
        System.out.println(10 % 2);   // 0, so 10 is even
        System.out.println(4520 % 10); // 0, the last digit

        // --- Integer Division vs Floating-point Division ---
        System.out.println(17 / 5);   // 3    int / int stays int
        System.out.println(17.0 / 5); // 3.4  one double makes it all decimal
        System.out.println(3 / 4);    // 0    0.75 with the decimal cut off
        System.out.println(3 / 4.0);  // 0.75
        // System.out.println(10 / 0); // crashes: ArithmeticException (try it, then comment it back out)

        // --- Integer Overflow ---
        int max = Integer.MAX_VALUE;
        System.out.println(max);      // 2147483647
        System.out.println(max + 1);  // -2147483648, it rolls over with no warning

        // --- Incrementing and Decrementing ---
        int j = 5;
        System.out.println(j++);      // 5: uses j, then adds 1
        System.out.println(++j);      // 7: adds 1, then uses j

        int l = 5;
        int result = l++ + ++l;       // 5 + 7
        System.out.println(result);   // 12
        System.out.println(l);        // 7

        // --- Compound Assignment Operators ---
        int count = 10;
        count += 5;                   // count = count + 5
        System.out.println(count);    // 15
        count *= 2;
        System.out.println(count);    // 30
        count %= 7;
        System.out.println(count);    // 2

        // --- String Concatenation ---
        System.out.println(1 + 2);       // 3
        System.out.println(1 + 2 + "3"); // 33  (1 + 2 is 3, then "3" is joined on)
        System.out.println("1" + 2 + 3); // 123 (once it's a String, everything after is joined)
        System.out.println("Total: " + count);

        // --- Order of Operations ---
        System.out.println(2 * 3 + 1);   // 7
        System.out.println(2 * (3 + 1)); // 8
    }
}
