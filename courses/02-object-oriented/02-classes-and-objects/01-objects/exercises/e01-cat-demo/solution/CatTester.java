public class CatTester {
    public static void main(String[] args) {
        // --- Making an Object ---
        Cat myCat;          // a variable that can hold a Cat (nothing in it yet)
        myCat = new Cat();  // make a Cat object

        // --- The Dot Operator ---
        myCat.meow();               // tell the cat to meow
        myCat.name = "Mr. Trinity"; // set its name
        myCat.walk(1.0);

        // --- Every Object Gets Its Own Values ---
        Cat otherCat = new Cat();
        otherCat.name = "Mochi";
        otherCat.walk(2.5);
        myCat.sleep();
    }
}
