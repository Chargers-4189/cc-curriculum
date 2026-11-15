// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("121")
    void case1() {
        TestUtil.assertOutput(Main.class, "121\n", "Enter a number: 121 reversed is 121\n121 is a palindrome");
    }

    @Test
    @DisplayName("456")
    void case2() {
        TestUtil.assertOutput(Main.class, "456\n", "Enter a number: 456 reversed is 654\n456 is not a palindrome");
    }

    @Test
    @DisplayName("4554")
    void case3() {
        TestUtil.assertOutput(Main.class, "4554\n", "Enter a number: 4554 reversed is 4554\n4554 is a palindrome");
    }

    @Test
    @DisplayName("One digit")
    void case4() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number: 7 reversed is 7\n7 is a palindrome");
    }

    @Test
    @DisplayName("Ends in 0")
    void case5() {
        TestUtil.assertOutput(Main.class, "120\n", "Enter a number: 120 reversed is 21\n120 is not a palindrome");
    }
}
