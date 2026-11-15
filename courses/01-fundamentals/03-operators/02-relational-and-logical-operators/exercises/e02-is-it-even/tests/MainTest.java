// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("10")
    void case1() {
        TestUtil.assertOutput(Main.class, "10\n", "Enter a number: Is even: true");
    }

    @Test
    @DisplayName("7")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number: Is even: false");
    }

    @Test
    @DisplayName("Zero")
    void case3() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter a number: Is even: true");
    }

    @Test
    @DisplayName("Negative even")
    void case4() {
        TestUtil.assertOutput(Main.class, "-4\n", "Enter a number: Is even: true");
    }
}
