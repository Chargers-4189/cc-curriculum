// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("4 rows")
    void case1() {
        TestUtil.assertOutput(Main.class, "4\n", "Enter the number of rows: *\n**\n***\n****");
    }

    @Test
    @DisplayName("1 row")
    void case2() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter the number of rows: *");
    }

    @Test
    @DisplayName("6 rows")
    void case3() {
        TestUtil.assertOutput(Main.class, "6\n", "Enter the number of rows: *\n**\n***\n****\n*****\n******");
    }
}
