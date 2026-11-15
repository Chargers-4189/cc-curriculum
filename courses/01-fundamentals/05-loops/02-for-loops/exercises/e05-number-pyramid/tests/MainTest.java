// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("5 lines")
    void case1() {
        TestUtil.assertOutput(Main.class, "5\n", "Enter the number of lines:               1\n           2  1  2\n        3  2  1  2  3\n     4  3  2  1  2  3  4\n  5  4  3  2  1  2  3  4  5");
    }

    @Test
    @DisplayName("1 line")
    void case2() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter the number of lines:   1");
    }

    @Test
    @DisplayName("3 lines")
    void case3() {
        TestUtil.assertOutput(Main.class, "3\n", "Enter the number of lines:         1\n     2  1  2\n  3  2  1  2  3");
    }

    @Test
    @DisplayName("12 lines (two digits)")
    void case4() {
        TestUtil.assertOutput(Main.class, "12\n", "Enter the number of lines:                                    1\n                                2  1  2\n                             3  2  1  2  3\n                          4  3  2  1  2  3  4\n                       5  4  3  2  1  2  3  4  5\n                    6  5  4  3  2  1  2  3  4  5  6\n                 7  6  5  4  3  2  1  2  3  4  5  6  7\n              8  7  6  5  4  3  2  1  2  3  4  5  6  7  8\n           9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9\n       10  9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9 10\n    11 10  9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9 10 11\n 12 11 10  9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9 10 11 12");
    }

    @Test
    @DisplayName("0 is too small")
    void case5() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter the number of lines: The number of lines must be from 1 to 15");
    }

    @Test
    @DisplayName("16 is too big")
    void case6() {
        TestUtil.assertOutput(Main.class, "16\n", "Enter the number of lines: The number of lines must be from 1 to 15");
    }
}
