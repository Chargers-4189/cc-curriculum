// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("March")
    void case1() {
        TestUtil.assertOutput(Main.class, "3\n", "Enter a month (1-12): March");
    }

    @Test
    @DisplayName("January")
    void case2() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter a month (1-12): January");
    }

    @Test
    @DisplayName("December")
    void case3() {
        TestUtil.assertOutput(Main.class, "12\n", "Enter a month (1-12): December");
    }

    @Test
    @DisplayName("13 is invalid")
    void case4() {
        TestUtil.assertOutput(Main.class, "13\n", "Enter a month (1-12): Invalid month");
    }

    @Test
    @DisplayName("0 is invalid")
    void case5() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter a month (1-12): Invalid month");
    }
}
