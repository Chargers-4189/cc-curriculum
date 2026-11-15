// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Prints the face")
    void case1() {
        TestUtil.assertOutput(Main.class, "", " _____\n| o o |\n|  ^  |\n|_____|");
    }
}
