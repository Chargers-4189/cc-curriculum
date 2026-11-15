// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Doubles 5")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n", "Enter a number: Doubled: 10");
    }

    @Test
    @DisplayName("Negative")
    void case2() {
        TestUtil.assertOutput(Main.class, "-3\n", "Enter a number: Doubled: -6");
    }
}
