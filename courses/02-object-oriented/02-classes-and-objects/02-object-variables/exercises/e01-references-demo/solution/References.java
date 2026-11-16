public class References {
    public static void main(String[] args) {
        // --- Two Kinds of Variables ---
        int x = 7;                             // primitive: the 7 is in x
        Person sue = new Person("Sue", 19);    // reference: sue holds a way to get to the Person
        System.out.println(sue.getName());

        // --- Copying a Primitive ---
        int a = 5;
        int b = a;     // copies the 5
        b = 10;
        System.out.println(a);                 // 5

        // --- Copying a Reference ---
        Person sally = sue;                    // copies the reference, not the person
        System.out.println(sally.getName());   // Sue

        // --- Changing an Object Through Another Variable ---
        Person joe = new Person("Joe", 37);
        Person chris = joe;
        chris.setName("Chris");
        System.out.println(joe.getName());     // Chris

        // --- null ---
        Person nobody = null;
        System.out.println(nobody);            // null
        // System.out.println(nobody.getName()); // crashes: NullPointerException
    }
}
