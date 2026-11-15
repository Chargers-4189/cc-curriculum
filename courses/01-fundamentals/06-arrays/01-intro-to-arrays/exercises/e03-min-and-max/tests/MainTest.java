// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Mixed")
    void case1() {
        TestUtil.assertOutput(Main.class, "7 2 9 4 6\n", "Enter 5 numbers: Min: 2\nMax: 9");
    }

    @Test
    @DisplayName("All negative")
    void case2() {
        TestUtil.assertOutput(Main.class, "-5 -2 -9 -1 -7\n", "Enter 5 numbers: Min: -9\nMax: -1");
    }

    @Test
    @DisplayName("All the same")
    void case3() {
        TestUtil.assertOutput(Main.class, "3 3 3 3 3\n", "Enter 5 numbers: Min: 3\nMax: 3");
    }

    @Test
    @DisplayName("Sorted")
    void case4() {
        TestUtil.assertOutput(Main.class, "1 2 3 4 5\n", "Enter 5 numbers: Min: 1\nMax: 5");
    }
}
