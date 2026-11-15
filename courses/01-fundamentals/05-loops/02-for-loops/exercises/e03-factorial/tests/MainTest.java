// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("5!")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n", "Enter n (0-20): 5! = 120");
    }

    @Test
    @DisplayName("0!")
    void case2() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter n (0-20): 0! = 1");
    }

    @Test
    @DisplayName("1!")
    void case3() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter n (0-20): 1! = 1");
    }

    @Test
    @DisplayName("13! needs a long")
    void case4() {
        TestUtil.assertOutput(Main.class, "13\n", "Enter n (0-20): 13! = 6227020800");
    }

    @Test
    @DisplayName("20!")
    void case5() {
        TestUtil.assertOutput(Main.class, "20\n", "Enter n (0-20): 20! = 2432902008176640000");
    }
}
