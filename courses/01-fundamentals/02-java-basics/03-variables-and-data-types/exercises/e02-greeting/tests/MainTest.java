// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Ada, 15")
    void case1() {
        TestUtil.assertOutput(Main.class, "Ada\n15\n", "Enter your name: Enter your age: Hi Ada, you are 15");
    }

    @Test
    @DisplayName("Grace, 17")
    void case2() {
        TestUtil.assertOutput(Main.class, "Grace\n17\n", "Enter your name: Enter your age: Hi Grace, you are 17");
    }

    @Test
    @DisplayName("Two-word name")
    void case3() {
        TestUtil.assertOutput(Main.class, "Mary Jane\n14\n", "Enter your name: Enter your age: Hi Mary Jane, you are 14");
    }
}
