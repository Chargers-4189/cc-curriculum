// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Four scores")
    void case1() {
        TestUtil.assertOutput(Main.class, "4\n70 80 90 100\n", "How many scores? Enter the scores: Average: 85.0\nAbove average: 2");
    }

    @Test
    @DisplayName("Uneven average")
    void case2() {
        TestUtil.assertOutput(Main.class, "3\n90 85 72\n", "How many scores? Enter the scores: Average: 82.33333333333333\nAbove average: 2");
    }

    @Test
    @DisplayName("All equal")
    void case3() {
        TestUtil.assertOutput(Main.class, "3\n50 50 50\n", "How many scores? Enter the scores: Average: 50.0\nAbove average: 0");
    }
}
