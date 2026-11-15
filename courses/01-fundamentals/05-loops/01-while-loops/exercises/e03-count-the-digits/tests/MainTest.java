// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("4520")
    void case1() {
        TestUtil.assertOutput(Main.class, "4520\n", "Enter a positive number: 4520 has 4 digits");
    }

    @Test
    @DisplayName("One digit")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a positive number: 7 has 1 digits");
    }

    @Test
    @DisplayName("Big number")
    void case3() {
        TestUtil.assertOutput(Main.class, "2147483647\n", "Enter a positive number: 2147483647 has 10 digits");
    }

    @Test
    @DisplayName("100")
    void case4() {
        TestUtil.assertOutput(Main.class, "100\n", "Enter a positive number: 100 has 3 digits");
    }
}
