// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("From 3")
    void case1() {
        TestUtil.assertOutput(Main.class, "3\n", "Enter a number: 3\n2\n1\nLiftoff!");
    }

    @Test
    @DisplayName("From 10")
    void case2() {
        TestUtil.assertOutput(Main.class, "10\n", "Enter a number: 10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nLiftoff!");
    }

    @Test
    @DisplayName("From 1")
    void case3() {
        TestUtil.assertOutput(Main.class, "1\n", "Enter a number: 1\nLiftoff!");
    }

    @Test
    @DisplayName("Zero")
    void case4() {
        TestUtil.assertOutput(Main.class, "0\n", "Enter a number: Liftoff!");
    }
}
