// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Middle is biggest")
    void case1() {
        TestUtil.assertOutput(Main.class, "4 9 2\n", "Enter three numbers: Max: 9");
    }

    @Test
    @DisplayName("Last is biggest")
    void case2() {
        TestUtil.assertOutput(Main.class, "1 2 3\n", "Enter three numbers: Max: 3");
    }

    @Test
    @DisplayName("First is biggest")
    void case3() {
        TestUtil.assertOutput(Main.class, "8 3 5\n", "Enter three numbers: Max: 8");
    }

    @Test
    @DisplayName("Negatives")
    void case4() {
        TestUtil.assertOutput(Main.class, "-4 -9 -2\n", "Enter three numbers: Max: -2");
    }

    @Test
    @DisplayName("Ties")
    void case5() {
        TestUtil.assertOutput(Main.class, "5 5 1\n", "Enter three numbers: Max: 5");
    }
}
