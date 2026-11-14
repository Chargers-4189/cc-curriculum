public class Methods {
    public static void main(String[] args) {
        /*
            int sum = 0;
            for (int i = 1; i <=10; i++) {
                sum += i;
            }
            System.out.println(sum);

            int sum = 0;
            for (int i = 20; i <= 37; i++) {
                sum += i;
            }
            System.out.println(sum);
        */
       System.out.println();
       sumOfRange(0, 0);
       System.out.println(sumOfRange(55,101));
       System.out.println(sumOfRange(67,72));
       System.out.println(sumOfRange(68,102));
       //Math.abs(1);
       System.out.println(absolute(-1));

       /*
       public static int max (int num1, int num2)
       -------------|---|---|--------------------
       modifers | return type | name of method | parameters

        What is the above method called? max
        What does it need? It needs an input of int num1, num2
        What datatype does it give back? integer
        What does this method do? Returns the max number 
       */
      // Which is better?
      // printGrade: 2
      // getGrade: 1
      printGrade(90.2);
      System.out.println(getGrade(99.3));
      //double grade = printGrade(20.3);

      /*
      getGrade: A method that RETURNS the grade can be printed,
      stored, compared, or fed into something.
      */
        int x = 1;
        System.out.println("Before: "+x);
        increment(x);
        System.out.println("After: "+x);

        int num1 = 1;
        int num2 = 2;
        System.out.println("Before: " + num1 + " " + num2);
        swap(num1, num2);
        System.out.println("After: " + num1 + " " + num2);

        /*
            Java passes a copy of the value. n1 and n2 are brand new
            variables that happen to start with the same values as num1
            and num2. Swapping the copies does nothing to the originals.
            When the methods ends, the copies are gone. This called scope
            a variable that is initilized and declared in a block/method
            does not exist outside the method.

            Declaring a variable in the header only exists within the method
            Parameters are just local variables that got their starting
            value from the caller.
        */
    }
    public static void swap(int n1, int n2) {
        int temp = n1;
        n1 = n2;
        n2 = temp;
        System.out.println("  inside swap: n1 = " + n1 + ", n2 = " + n2);
    }
    public static void increment(int n) {
        n++;
        System.out.println("n inside the method is " + n);
    }

    public static void printGrade(double grade) {
        System.out.println(grade);
    }
    public static double getGrade(double grade) {
        return grade;
    }
    public static int sumOfRange(int min, int max) {
        int sum = 0;
        // for (initialization; condition; increment)
        for (; min <= max; min++){
            sum += min;
        }
        return sum;
    }

    public static int absolute(int a) {
        if (a <= 0) {
            a = a * -1;
        }
        return a;
    }
}
