// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Three items")
    void case1() {
        TestUtil.assertOutput(Main.class, "zip ties\nduct tape\nbolts\ndone\n", "Enter items, then done:\nYou have 3 items:\n1. zip ties\n2. duct tape\n3. bolts");
    }

    @Test
    @DisplayName("One item")
    void case2() {
        TestUtil.assertOutput(Main.class, "pizza\ndone\n", "Enter items, then done:\nYou have 1 items:\n1. pizza");
    }

    @Test
    @DisplayName("Nothing")
    void case3() {
        TestUtil.assertOutput(Main.class, "done\n", "Enter items, then done:\nYou have 0 items:");
    }
}
