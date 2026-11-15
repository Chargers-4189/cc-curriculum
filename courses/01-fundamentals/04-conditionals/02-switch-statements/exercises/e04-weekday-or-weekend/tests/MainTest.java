// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Saturday")
    void case1() {
        TestUtil.assertOutput(Main.class, "6\n", "Enter a day (1-7): Weekend");
    }

    @Test
    @DisplayName("Sunday")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a day (1-7): Weekend");
    }

    @Test
    @DisplayName("Monday")
    void case3() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter a day (1-7): Weekday");
    }

    @Test
    @DisplayName("Friday")
    void case4() {
        TestUtil.assertOutput(Main.class, "5\n", "Enter a day (1-7): Weekday");
    }

    @Test
    @DisplayName("8 is invalid")
    void case5() {
        TestUtil.assertOutput(Main.class, "8\n", "Enter a day (1-7): Invalid day");
    }
}
