// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "speed 3, color yellow, radius 10.0\ncolor blue, radius 5.0, fan is off\nspeed 2, color blue, radius 5.0\nIs the first fan on? true");
    }
}
