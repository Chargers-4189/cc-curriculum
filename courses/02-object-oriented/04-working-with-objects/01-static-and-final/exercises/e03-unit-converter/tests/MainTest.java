// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "10 feet is 3.05 meters\n2 meters is 6.56 feet\n120 pounds is 54.43 kilograms\nOne foot is 0.3048 meters");
    }
}
