// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("5 and 3")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n3\n", "Enter a: Enter b: a = 3, b = 5");
    }

    @Test
    @DisplayName("Same numbers")
    void case2() {
        TestUtil.assertOutput(Main.class, "4\n4\n", "Enter a: Enter b: a = 4, b = 4");
    }

    @Test
    @DisplayName("Negatives")
    void case3() {
        TestUtil.assertOutput(Main.class, "-1\n10\n", "Enter a: Enter b: a = 10, b = -1");
    }
}
