// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("1 to 5")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n1 2 3 4 5\n", "How many numbers? Enter the numbers: 5 4 3 2 1");
    }

    @Test
    @DisplayName("One number")
    void case2() {
        TestUtil.assertOutput(Main.class, "1\n42\n", "How many numbers? Enter the numbers: 42");
    }

    @Test
    @DisplayName("Mixed")
    void case3() {
        TestUtil.assertOutput(Main.class, "4\n10 -3 7 0\n", "How many numbers? Enter the numbers: 0 7 -3 10");
    }
}
