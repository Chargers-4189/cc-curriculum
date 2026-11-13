import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

// Delete this tests/ folder if the exercise doesn't need automatic checking.
class ExerciseTest {
    @Test
    @Disabled("TODO: write tests")
    void printsExpectedOutput() {
        String out = TestUtil.runMain(Exercise.class, "" /* stdin */);
        assertEquals("", out.strip());
    }
}
