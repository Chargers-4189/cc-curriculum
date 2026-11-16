// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Runs main")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "Playing the movie Iron Lung\nPlaying the movie Toy Story 5\nIron Lung is rated 9\nToy Story 5 is a Comedy movie");
    }
}
