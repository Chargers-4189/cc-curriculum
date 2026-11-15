// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("85 is a B")
    void case1() {
        TestUtil.assertOutput(Main.class, "85\n", "Enter your score: Grade: B");
    }

    @Test
    @DisplayName("Exactly 90")
    void case2() {
        TestUtil.assertOutput(Main.class, "90\n", "Enter your score: Grade: A");
    }

    @Test
    @DisplayName("100")
    void case3() {
        TestUtil.assertOutput(Main.class, "100\n", "Enter your score: Grade: A");
    }

    @Test
    @DisplayName("72")
    void case4() {
        TestUtil.assertOutput(Main.class, "72\n", "Enter your score: Grade: C");
    }

    @Test
    @DisplayName("Exactly 60")
    void case5() {
        TestUtil.assertOutput(Main.class, "60\n", "Enter your score: Grade: D");
    }

    @Test
    @DisplayName("59")
    void case6() {
        TestUtil.assertOutput(Main.class, "59\n", "Enter your score: Grade: F");
    }
}
