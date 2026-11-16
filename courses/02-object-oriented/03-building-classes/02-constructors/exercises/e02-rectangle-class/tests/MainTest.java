// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "1.0 x 1.0: area 1.0, perimeter 4.0\n4.0 x 40.0: area 160.0, perimeter 88.0\n3.5 x 2.0: area 7.0, perimeter 11.0");
    }
}
