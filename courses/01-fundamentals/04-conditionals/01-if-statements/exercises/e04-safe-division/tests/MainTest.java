// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("10 / 3")
    void case1() {
        TestUtil.assertOutput(Main.class, "10\n3\n", "Enter the dividend: Enter the divisor: 10 / 3 = 3");
    }

    @Test
    @DisplayName("Divide by zero")
    void case2() {
        TestUtil.assertOutput(Main.class, "10\n0\n", "Enter the dividend: Enter the divisor: Cannot divide by zero");
    }

    @Test
    @DisplayName("Negative")
    void case3() {
        TestUtil.assertOutput(Main.class, "-9\n2\n", "Enter the dividend: Enter the divisor: -9 / 2 = -4");
    }

    @Test
    @DisplayName("Zero on top")
    void case4() {
        TestUtil.assertOutput(Main.class, "0\n5\n", "Enter the dividend: Enter the divisor: 0 / 5 = 0");
    }
}
