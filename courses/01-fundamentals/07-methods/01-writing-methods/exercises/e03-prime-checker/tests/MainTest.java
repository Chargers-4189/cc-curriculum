// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("7")
    void case1() {
        TestUtil.assertOutput(Main.class, "7\n", "Enter a number: 7 is prime");
    }

    @Test
    @DisplayName("8")
    void case2() {
        TestUtil.assertOutput(Main.class, "8\n", "Enter a number: 8 is not prime");
    }

    @Test
    @DisplayName("2 is prime")
    void case3() {
        TestUtil.assertOutput(Main.class, "2\n", "Enter a number: 2 is prime");
    }

    @Test
    @DisplayName("1 is not prime")
    void case4() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter a number: 1 is not prime");
    }

    @Test
    @DisplayName("97")
    void case5() {
        TestUtil.assertOutput(Main.class, "97\n", "Enter a number: 97 is prime");
    }

    @Test
    @DisplayName("91 = 7 * 13")
    void case6() {
        TestUtil.assertOutput(Main.class, "91\n", "Enter a number: 91 is not prime");
    }
}
