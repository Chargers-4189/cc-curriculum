// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Same")
    void case1() {
        TestUtil.assertOutput(Main.class, "robot\nrobot\n", "Enter the first word: Enter the second word: Same word: true");
    }

    @Test
    @DisplayName("Different")
    void case2() {
        TestUtil.assertOutput(Main.class, "robot\nmotor\n", "Enter the first word: Enter the second word: Same word: false");
    }

    @Test
    @DisplayName("Capitals count")
    void case3() {
        TestUtil.assertOutput(Main.class, "Robot\nrobot\n", "Enter the first word: Enter the second word: Same word: false");
    }
}
