// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("7.89")
    void case1() {
        TestUtil.assertOutput(Main.class, "7.89\n", "Enter a decimal: Whole part: 7");
    }

    @Test
    @DisplayName("3.0")
    void case2() {
        TestUtil.assertOutput(Main.class, "3.0\n", "Enter a decimal: Whole part: 3");
    }

    @Test
    @DisplayName("Negative")
    void case3() {
        TestUtil.assertOutput(Main.class, "-2.5\n", "Enter a decimal: Whole part: -2");
    }

    @Test
    @DisplayName("Just under 1")
    void case4() {
        TestUtil.assertOutput(Main.class, "0.99\n", "Enter a decimal: Whole part: 0");
    }
}
