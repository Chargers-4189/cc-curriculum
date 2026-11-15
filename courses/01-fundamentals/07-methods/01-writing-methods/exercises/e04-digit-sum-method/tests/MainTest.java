// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("4520")
    void case1() {
        TestUtil.assertOutput(Main.class, "4520\n", "Enter a number: Sum of digits: 11");
    }

    @Test
    @DisplayName("234")
    void case2() {
        TestUtil.assertOutput(Main.class, "234\n", "Enter a number: Sum of digits: 9");
    }

    @Test
    @DisplayName("One digit")
    void case3() {
        TestUtil.assertOutput(Main.class, "8\n", "Enter a number: Sum of digits: 8");
    }

    @Test
    @DisplayName("Long number")
    void case4() {
        TestUtil.assertOutput(Main.class, "9876543210123\n", "Enter a number: Sum of digits: 51");
    }
}
