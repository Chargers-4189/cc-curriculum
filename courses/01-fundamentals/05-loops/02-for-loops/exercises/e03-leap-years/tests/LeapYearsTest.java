import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class LeapYearsTest {
    private static List<List<Integer>> yearLines = new ArrayList<>();
    private static String lastLine = "";
    private static List<Integer> expected = new ArrayList<>();

    @BeforeAll
    static void run() {
        for (int y = 101; y <= 2100; y++) {
            if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) expected.add(y);
        }
        String out = TestUtil.runMain(LeapYears.class);
        for (String line : out.split("\n")) {
            String t = line.trim();
            if (t.isEmpty()) continue;
            lastLine = t;
            if (t.matches("[0-9]+( [0-9]+)*")) {          // a line of years, one space apart
                List<Integer> years = new ArrayList<>();
                for (String s : t.split(" ")) years.add(Integer.parseInt(s));
                yearLines.add(years);
            }
        }
    }

    @Test
    void printsEveryLeapYearInOrder() {
        List<Integer> printed = new ArrayList<>();
        yearLines.forEach(printed::addAll);
        assertFalse(printed.isEmpty(), "No lines of years separated by single spaces were found");
        assertEquals(expected.get(0), printed.get(0), "The first leap year after 101 is 104");
        assertEquals(expected, printed, "The years printed are not exactly the leap years from 101 to 2100");
    }

    @Test
    void tenYearsPerLine() {
        for (int i = 0; i < yearLines.size() - 1; i++) {
            assertEquals(10, yearLines.get(i).size(), "Line " + (i + 1) + " should have 10 years");
        }
        int last = yearLines.get(yearLines.size() - 1).size();
        assertTrue(last >= 1 && last <= 10, "The last line of years should have 1 to 10 years");
    }

    @Test
    void printsTheTotal() {
        assertTrue(lastLine.contains(String.valueOf(expected.size())) && !lastLine.matches("[0-9 ]+"),
                "The last line should report the total number of leap years (" + expected.size() + "), but was: " + lastLine);
    }
}
