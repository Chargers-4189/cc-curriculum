// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Boiling")
    void case1() {
        TestUtil.assertOutput(Main.class, "212\n", "Enter degrees Fahrenheit: Celsius: 100.0");
    }

    @Test
    @DisplayName("Freezing")
    void case2() {
        TestUtil.assertOutput(Main.class, "32\n", "Enter degrees Fahrenheit: Celsius: 0.0");
    }

    @Test
    @DisplayName("-40")
    void case3() {
        TestUtil.assertOutput(Main.class, "-40\n", "Enter degrees Fahrenheit: Celsius: -40.0");
    }

    @Test
    @DisplayName("Room temperature")
    void case4() {
        TestUtil.assertOutput(Main.class, "68\n", "Enter degrees Fahrenheit: Celsius: 20.0");
    }
}
