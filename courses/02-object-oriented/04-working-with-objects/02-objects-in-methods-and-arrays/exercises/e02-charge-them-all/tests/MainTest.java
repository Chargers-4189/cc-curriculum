// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Bolt: 40%\nVolt: 90%\nAmp: 10%\nAfter charging:\nBolt: 65%\nVolt: 100%\nAmp: 35%");
    }
}
