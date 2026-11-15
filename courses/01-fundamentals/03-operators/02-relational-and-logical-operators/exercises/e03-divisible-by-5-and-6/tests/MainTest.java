// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("10")
    void case1() {
        TestUtil.assertOutput(Main.class, "10\n", "Enter a number: Divisible by 5 and 6: false\nDivisible by 5 or 6: true\nDivisible by 5 or 6, but not both: true");
    }

    @Test
    @DisplayName("30")
    void case2() {
        TestUtil.assertOutput(Main.class, "30\n", "Enter a number: Divisible by 5 and 6: true\nDivisible by 5 or 6: true\nDivisible by 5 or 6, but not both: false");
    }

    @Test
    @DisplayName("7")
    void case3() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number: Divisible by 5 and 6: false\nDivisible by 5 or 6: false\nDivisible by 5 or 6, but not both: false");
    }

    @Test
    @DisplayName("18")
    void case4() {
        TestUtil.assertOutput(Main.class, "18\n", "Enter a number: Divisible by 5 and 6: false\nDivisible by 5 or 6: true\nDivisible by 5 or 6, but not both: true");
    }
}
