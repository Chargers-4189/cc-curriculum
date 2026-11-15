// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("7 * 3")
    void case1() {
        TestUtil.assertOutput(Main.class, "7\n*\n3\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: 7 * 3 = 21");
    }

    @Test
    @DisplayName("Add")
    void case2() {
        TestUtil.assertOutput(Main.class, "12\n+\n30\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: 12 + 30 = 42");
    }

    @Test
    @DisplayName("Subtract")
    void case3() {
        TestUtil.assertOutput(Main.class, "5\n-\n9\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: 5 - 9 = -4");
    }

    @Test
    @DisplayName("Divide")
    void case4() {
        TestUtil.assertOutput(Main.class, "17\n/\n5\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: 17 / 5 = 3");
    }

    @Test
    @DisplayName("Remainder")
    void case5() {
        TestUtil.assertOutput(Main.class, "17\n%\n5\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: 17 % 5 = 2");
    }

    @Test
    @DisplayName("Unknown")
    void case6() {
        TestUtil.assertOutput(Main.class, "2\n^\n3\n", "Enter a number: Enter an operator (+ - * / %): Enter another number: Unknown operator");
    }
}
