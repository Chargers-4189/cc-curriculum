// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Three scores")
    void case1() {
        TestUtil.assertOutput(Main.class, "90\n80\n75\n-1\n", "Enter a score (-1 to stop): Enter a score (-1 to stop): Enter a score (-1 to stop): Enter a score (-1 to stop): Count: 3\nAverage: 81.66666666666667");
    }

    @Test
    @DisplayName("One score")
    void case2() {
        TestUtil.assertOutput(Main.class, "100\n-1\n", "Enter a score (-1 to stop): Enter a score (-1 to stop): Count: 1\nAverage: 100.0");
    }

    @Test
    @DisplayName("No scores")
    void case3() {
        TestUtil.assertOutput(Main.class, "-1\n", "Enter a score (-1 to stop): No scores entered");
    }

    @Test
    @DisplayName("Even average")
    void case4() {
        TestUtil.assertOutput(Main.class, "70\n80\n-1\n", "Enter a score (-1 to stop): Enter a score (-1 to stop): Enter a score (-1 to stop): Count: 2\nAverage: 75.0");
    }
}
