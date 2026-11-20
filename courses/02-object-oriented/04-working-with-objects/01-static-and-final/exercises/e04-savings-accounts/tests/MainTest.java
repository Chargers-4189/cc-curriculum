// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Account #1001: $20000.0\nAccount #1002: $1200.0\nQuinn earns $75.00 a month\nCaleb earns $4.50 a month\nThe rate is now 6.0%\nQuinn earns $100.00 a month\nCaleb earns $7.50 a month\nCaleb has $1500.0");
    }
}
