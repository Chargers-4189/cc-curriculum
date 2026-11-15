// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("32 to 212")
    void case1() {
        TestUtil.assertOutput(Main.class, "32 212 45\n", "Enter start, end, and step: 32 0\n77 25\n122 50\n167 75\n212 100");
    }

    @Test
    @DisplayName("Small steps")
    void case2() {
        TestUtil.assertOutput(Main.class, "0 40 10\n", "Enter start, end, and step: 0 -17\n10 -12\n20 -6\n30 -1\n40 4");
    }

    @Test
    @DisplayName("One row")
    void case3() {
        TestUtil.assertOutput(Main.class, "212 212 1\n", "Enter start, end, and step: 212 100");
    }
}
