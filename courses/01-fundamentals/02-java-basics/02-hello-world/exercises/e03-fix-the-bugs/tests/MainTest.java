// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Prints both lines")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "I can fix bugs!\nJava is picky.");
    }
}
