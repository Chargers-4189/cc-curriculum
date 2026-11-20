// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Before: [4, -2, -7, 5, -1, 8]\nAfter: [4, 5, 8]");
    }
}
