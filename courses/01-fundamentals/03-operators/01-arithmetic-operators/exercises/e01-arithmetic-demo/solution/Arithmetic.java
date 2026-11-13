public class Arithmetic {
    public static void main(String[] args) {
        int a = 17, b = 5;
        // --- Basic Math Operators ---
        System.out.println(a + b); // 22
        System.out.println(a - b); // 12
        System.out.println(a * b); // 85
        System.out.println(a / b); // 3
        System.out.println(a % b); // 2 = This gives us the remainder after a / b

        // --- Integer Division vs Floating-point division
        // Integer: whole numbers
        // Double: decimal numbers
        System.out.println(a / b); // Integers: 3
        double c = 17.0, d = 5.0;
        System.out.println(c / d); // Double: 3.4
        // Floating division: If EITHER value is a double/float in a division
        // then the whole expression is calculated as a floating-point (decimal)
        // If both are integers: it is calculated as integer division

        System.out.println(a / d); // 3.4

        // --- Integer Overflow ---
        int max = Integer.MAX_VALUE;
        System.out.println(max + 1);
        // When adding to integer max, it will roll over to negative minimum: -2147483648

        // Incrementing and decrementing
        int j = 5;
        // ++ is equivalent j = j + 1
        // -- is equivalent j = j - 1
        System.out.println(j++); // Uses j first, then add 1: prints 5
        System.out.println(++j); // Adds 1, then uses j: prints 7
        int k = 5;
        System.out.println(++k); // 6
        System.out.println(k);   // 6

        int l = 5;
        int result = l++ + ++l; // 5 + 7
        System.out.println(result); // 12
        System.out.println(l);      // 7

        // --- Compound assignment operators ---
        int count = 10;
        count = count + 1; // 11
        count++;           // 12
        count += 1;        // 13
        System.out.println(count); // 13
        count *= 10;
        System.out.println(count); // 130
        count /= 10;
        System.out.println(count); // 13

        // --- String concatenation ---
        System.out.println(1 + 2);       // 3
        System.out.println(1 + 2 + "3"); // 33  (1 + 2 = 3, then "3" is joined on)
        System.out.println("1" + 2 + 3); // 123 (once it's a String, everything after is joined)
    }
}
