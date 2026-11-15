// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Positive")
    void case1() {
        TestUtil.assertOutput(Main.class, "12\n", "Enter a number: Positive");
    }

    @Test
    @DisplayName("Negative")
    void case2() {
        TestUtil.assertOutput(Main.class, "-8\n", "Enter a number: Negative");
    }

    @Test
    @DisplayName("Zero")
    void case3() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter a number: Zero");
    }
}
