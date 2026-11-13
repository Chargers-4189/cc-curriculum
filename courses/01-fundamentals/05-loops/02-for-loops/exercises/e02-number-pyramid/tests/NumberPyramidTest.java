import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class NumberPyramidTest {
    /** The pyramid rows, with spacing ignored and the prompt removed. */
    private static List<String> rows(int lines) {
        String out = TestUtil.runMain(NumberPyramid.class, lines + "\n");
        out = out.replace("Enter the number of lines:", "\n");
        List<String> rows = new ArrayList<>();
        for (String line : out.split("\n")) {
            String clean = line.trim().replaceAll("\\s+", " ");
            if (!clean.isEmpty()) {
                rows.add(clean);
            }
        }
        return rows;
    }

    private static String expectedRow(int row) {
        StringBuilder sb = new StringBuilder();
        for (int n = row; n >= 1; n--) sb.append(n).append(' ');
        for (int n = 2; n <= row; n++) sb.append(n).append(' ');
        return sb.toString().trim();
    }

    @Test
    void fiveLinesMatchesTheExample() {
        assertEquals(List.of("1", "2 1 2", "3 2 1 2 3", "4 3 2 1 2 3 4", "5 4 3 2 1 2 3 4 5"), rows(5));
    }

    @ParameterizedTest(name = "{0} lines")
    @ValueSource(ints = {1, 2, 9, 15})
    void everyRowIsCorrect(int lines) {
        List<String> rows = rows(lines);
        assertEquals(lines, rows.size(), "Expected " + lines + " rows but got " + rows.size() + ":\n" + String.join("\n", rows));
        for (int row = 1; row <= lines; row++) {
            assertEquals(expectedRow(row), rows.get(row - 1), "Row " + row + " is wrong");
        }
    }

    @Test
    void rowsAreCentered() {
        String out = TestUtil.runMain(NumberPyramid.class, "5\n").replace("Enter the number of lines:", "\n");
        List<String> lines = new ArrayList<>();
        for (String line : out.split("\n")) {
            if (!line.isBlank()) lines.add(line.replaceAll("\\s+$", ""));
        }
        String first = lines.get(0), last = lines.get(lines.size() - 1);
        int firstIndent = first.length() - first.stripLeading().length();
        int lastIndent = last.length() - last.stripLeading().length();
        assertTrue(firstIndent > lastIndent, "The top row should be indented more than the bottom row so the pyramid is centered");
    }
}
