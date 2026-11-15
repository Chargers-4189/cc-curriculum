// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("3")
    void case1() {
        TestUtil.assertOutput(Main.class, "3\n", "Enter a number: 3 6 9 12 15");
    }

    @Test
    @DisplayName("7")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number: 7 14 21 28 35");
    }

    @Test
    @DisplayName("1")
    void case3() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter a number: 1 2 3 4 5");
    }

    @Test
    @DisplayName("Zero")
    void case4() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter a number: 0 0 0 0 0");
    }
}
