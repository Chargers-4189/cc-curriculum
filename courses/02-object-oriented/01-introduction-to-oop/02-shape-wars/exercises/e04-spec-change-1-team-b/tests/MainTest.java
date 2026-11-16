// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("All four shapes")
    void case1() {
        TestUtil.assertOutput(Main.class, "", "--- user clicked the square ---\nRotating the square 360 degrees around (25.0, 25.0)\nPlaying square.wav\n\n--- user clicked the circle ---\nRotating the circle 360 degrees around (20.0, 20.0)\nPlaying circle.wav\n\n--- user clicked the triangle ---\nRotating the triangle 360 degrees around (30.0, 15.0)\nPlaying triangle.wav\n\n--- user clicked the amoeba ---\nRotating the amoeba 360 degrees around (17.5, 10.0)\nPlaying amoeba.mp3");
    }
}
