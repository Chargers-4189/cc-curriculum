import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDate;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class DayOfWeekTest {
    private static String expectedDay(int year, int month, int day) {
        String name = LocalDate.of(year, month, day).getDayOfWeek().toString(); // e.g. SUNDAY
        return name.charAt(0) + name.substring(1).toLowerCase();               // Sunday
    }

    @ParameterizedTest(name = "{0}-{1}-{2}")
    @CsvSource({
        "2015, 1, 25",   // the example in the prompt (January)
        "2012, 5, 12",
        "2000, 2, 29",   // leap day, February
        "2026, 8, 10",
        "2024, 12, 25",
        "1999, 12, 31",
        "2023, 3, 1",
        "2021, 1, 1",
        "1900, 2, 28",
    })
    void printsTheCorrectDay(int year, int month, int day) {
        String out = TestUtil.runMain(DayOfWeek.class, year + "\n" + month + "\n" + day + "\n");
        String expected = "Day of the week is " + expectedDay(year, month, day);
        assertTrue(out.contains(expected),
                "For " + year + "-" + month + "-" + day + " expected \"" + expected + "\" but the output was:\n" + out);
    }
}
