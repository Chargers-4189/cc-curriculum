// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Friday + 50")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n50\n", "Enter today's day (1 = Monday ... 7 = Sunday): Enter the number of days: In 50 days it will be day 6");
    }

    @Test
    @DisplayName("Sunday + 1 wraps to Monday")
    void case2() {
        TestUtil.assertOutput(Main.class, "7\n1\n", "Enter today's day (1 = Monday ... 7 = Sunday): Enter the number of days: In 1 days it will be day 1");
    }

    @Test
    @DisplayName("Monday + 0")
    void case3() {
        TestUtil.assertOutput(Main.class, "1\n0\n", "Enter today's day (1 = Monday ... 7 = Sunday): Enter the number of days: In 0 days it will be day 1");
    }

    @Test
    @DisplayName("Wednesday + 365")
    void case4() {
        TestUtil.assertOutput(Main.class, "3\n365\n", "Enter today's day (1 = Monday ... 7 = Sunday): Enter the number of days: In 365 days it will be day 4");
    }

    @Test
    @DisplayName("Saturday + 8")
    void case5() {
        TestUtil.assertOutput(Main.class, "6\n8\n", "Enter today's day (1 = Monday ... 7 = Sunday): Enter the number of days: In 8 days it will be day 7");
    }
}
