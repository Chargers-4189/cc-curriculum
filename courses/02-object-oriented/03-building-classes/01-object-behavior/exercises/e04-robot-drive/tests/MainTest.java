// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Bolt drove 10 meters\nBolt doesn't have enough battery to drive 20 meters\nBolt drove 15 meters\nBattery: 0%\nDistance: 25 meters\nBattery: 80%\nBolt drove 15 meters\nDistance: 40 meters");
    }
}
