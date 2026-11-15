// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Three students")
    void case1() {
        TestUtil.assertOutput(Main.class, "3\n95 82 67\n", "How many students? Enter the scores: Student 1: 95 (A)\nStudent 2: 82 (B)\nStudent 3: 67 (D)\nAverage: 81.33333333333333\nHighest: 95");
    }

    @Test
    @DisplayName("One student")
    void case2() {
        TestUtil.assertOutput(Main.class, "1\n100\n", "How many students? Enter the scores: Student 1: 100 (A)\nAverage: 100.0\nHighest: 100");
    }

    @Test
    @DisplayName("Every grade")
    void case3() {
        TestUtil.assertOutput(Main.class, "5\n91 85 74 60 12\n", "How many students? Enter the scores: Student 1: 91 (A)\nStudent 2: 85 (B)\nStudent 3: 74 (C)\nStudent 4: 60 (D)\nStudent 5: 12 (F)\nAverage: 64.4\nHighest: 91");
    }
}
