// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Prints all three lines")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Java is fun!\nRobots are cooler.\nLet's build one.");
    }
}
