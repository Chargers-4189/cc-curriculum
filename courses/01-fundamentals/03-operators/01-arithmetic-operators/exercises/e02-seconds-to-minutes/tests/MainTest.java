// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("500")
    void case1() {
        TestUtil.assertOutput(Main.class, "500\n", "Enter seconds: 500 seconds is 8 minutes and 20 seconds");
    }

    @Test
    @DisplayName("Exactly 2 minutes")
    void case2() {
        TestUtil.assertOutput(Main.class, "120\n", "Enter seconds: 120 seconds is 2 minutes and 0 seconds");
    }

    @Test
    @DisplayName("Under a minute")
    void case3() {
        TestUtil.assertOutput(Main.class, "45\n", "Enter seconds: 45 seconds is 0 minutes and 45 seconds");
    }

    @Test
    @DisplayName("1000")
    void case4() {
        TestUtil.assertOutput(Main.class, "1000\n", "Enter seconds: 1000 seconds is 16 minutes and 40 seconds");
    }
}
