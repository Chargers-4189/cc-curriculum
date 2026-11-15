// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("January 25, 2015")
    void case1() {
        TestUtil.assertOutput(Main.class, "2015\n1\n25\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Sunday");
    }

    @Test
    @DisplayName("May 12, 2012")
    void case2() {
        TestUtil.assertOutput(Main.class, "2012\n5\n12\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Saturday");
    }

    @Test
    @DisplayName("Leap day 2000")
    void case3() {
        TestUtil.assertOutput(Main.class, "2000\n2\n29\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Tuesday");
    }

    @Test
    @DisplayName("December 31, 1999")
    void case4() {
        TestUtil.assertOutput(Main.class, "1999\n12\n31\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Friday");
    }

    @Test
    @DisplayName("March 1, 2023")
    void case5() {
        TestUtil.assertOutput(Main.class, "2023\n3\n1\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Wednesday");
    }

    @Test
    @DisplayName("January 1, 2021")
    void case6() {
        TestUtil.assertOutput(Main.class, "2021\n1\n1\n", "Enter year: (e.g., 2012): Enter month: 1-12: Enter the day of the month: 1-31: Day of the week is Friday");
    }
}
