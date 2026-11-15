// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("4, -8, 1")
    void case1() {
        TestUtil.assertOutput(Main.class, "4 -8 1\n", "Enter a, b, c: Roots: 1.8660254037844386 and 0.1339745962155614");
    }

    @Test
    @DisplayName("No real roots")
    void case2() {
        TestUtil.assertOutput(Main.class, "1 0 1\n", "Enter a, b, c: No real roots");
    }

    @Test
    @DisplayName("Whole-number roots")
    void case3() {
        TestUtil.assertOutput(Main.class, "1 -3 2\n", "Enter a, b, c: Roots: 2.0 and 1.0");
    }

    @Test
    @DisplayName("One repeated root")
    void case4() {
        TestUtil.assertOutput(Main.class, "1 2 1\n", "Enter a, b, c: Roots: -1.0 and -1.0");
    }

    @Test
    @DisplayName("Needs (2 * a)")
    void case5() {
        TestUtil.assertOutput(Main.class, "2 -10 12\n", "Enter a, b, c: Roots: 3.0 and 2.0");
    }
}
