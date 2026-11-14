import java.util.Scanner;

public class Loops {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
        /*
        1. WHILE: the two basic things every loop needs
        */
        int sum = 0, i = 1;
        while (i < 10) {
            sum += i;
            i++;
        } 
        System.out.println(sum);
        /*
        while (loop-continuation condition) {
            Loop body
        }
        loop continuation condition = Runs the loop when true

        Every loop needs:
        1. Something inside the body that changes
        2. A condition that eventually becomes false because of that change.

        Steps to create a while loop:
        1. Write the code to do the thing once to get it working
        2. Wrap it in a while (true) { ... }
        3. Replace true with a real condition, and add whatever statement makes
        that condition eventually become false.
        */
    System.out.println("Enter an integer (ends if it is 0): ");
    int data = input.nextInt();
    int total = 0;
    while (data != 0) {
        total += data;
        System.out.println("Enter an integer (ends if it is 0): ");
        data = input.nextInt();
    }
    System.out.println("Sum is " + total);

    /*
        Every counting while loop has the same three parts,
        and in a whileloop they're scattered across three
        different places:
        int k = 0; <- initialization (above the loop)
        while (k < 10) { <- condition
            ...
            k++; <- update
        }
        for loops put all three in the header where you can see
    */
    for (int k = 0; k < 10; k++) {
        System.out.println("Welcome to Java!");
    }
    /*
    Order of execution
    1. init runs once
    2. condition checked -> if false, stop
    3. body runs
    4. update runs
    5. return to step 2
    for ([1], [2], [4]) {
        [3];
    }

    A variable declared in the header only exists inside the loop
    */
    for (int k = 5; k >= 1; k--) {
        System.out.print(k + " ");
    }
    System.out.println();
    for (int j = 0; j <= 10; j++) {
        System.out.println(j);
        j++; // j goes up twice per pass, so this prints every other number
    }
    /*
        What loop should I use?
        for -> I know how many times (print 10 rows, 1 to 100)
        while -> I don't (until the user types 0, until they guess it)
        Pick the best one that makes the code readable.
    */
    /*
    Nested For Loops (loops inside loops)
    */
    for (int row = 1; row <= 9; row++) {
            System.out.print(row + " | ");
            for (int col = 1; col <= 9; col++) {
                System.out.printf("%4d", row * col);
            }
            System.out.println();
    }
    // Warning for nested loops: three nested loops of 10,000
    // is a trillion loops (lots of compute)
    /*
        break = Get out of a loop
        continue = Skip to next iteration

        Both are conveniences, can be written with a boolean flag
        instead. Be wary of multiple breaks, multiple exists can
        become confusing to follow in a loop.
        
        In a nested loop, break only exits the inner loop.
    */
        // Break
        int bSum = 0;
        for (int n = 1; n <=20; n++) {
            bSum += n;
            if (bSum >= 100) {
                break;
            }
        }
        System.out.println("Stopped at sum = " + bSum);

        // Continue
        int cSum = 0;
        for (int n = 1; n <= 20; n++) {
            if (n % 2 == 0)
                continue; // skip the REST of this pass, go to the next n
            cSum += n;
        }
        System.out.println("Sum of odds = " + cSum);
    
    }
}
