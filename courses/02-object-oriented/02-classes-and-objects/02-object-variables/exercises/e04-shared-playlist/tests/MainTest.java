// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Road Trip: 3 songs\nRoad Trip: 3 songs\nGym: 2 songs\nRoad Trip: 3 songs\nGym: 3 songs\nGym: 3 songs");
    }
}
