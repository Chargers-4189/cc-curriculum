// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("932")
    void case1() {
        TestUtil.assertOutput(Main.class, "932\n", "Enter a number between 0 and 999: The sum of the digits is 14");
    }

    @Test
    @DisplayName("Single digit")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number between 0 and 999: The sum of the digits is 7");
    }

    @Test
    @DisplayName("999")
    void case3() {
        TestUtil.assertOutput(Main.class, "999\n", "Enter a number between 0 and 999: The sum of the digits is 27");
    }

    @Test
    @DisplayName("Zero in the middle")
    void case4() {
        TestUtil.assertOutput(Main.class, "405\n", "Enter a number between 0 and 999: The sum of the digits is 9");
    }
}
