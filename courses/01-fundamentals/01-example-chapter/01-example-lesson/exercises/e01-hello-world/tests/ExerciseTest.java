import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ExerciseTest {
    @Test
    void printsHelloWorld() {
        String out = TestUtil.runMain(Exercise.class);
        assertEquals("Hello, world!", out.strip());
    }
}
