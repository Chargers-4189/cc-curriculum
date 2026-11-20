// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Played: 4\nRed won: 2\nHighest scoring: match 3\nRed won: 3");
    }
}
