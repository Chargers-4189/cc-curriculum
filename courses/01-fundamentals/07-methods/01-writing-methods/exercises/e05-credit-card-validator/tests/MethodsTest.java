import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class MethodsTest {
    @Test
    void getDigit() {
        assertEquals(7, Main.getDigit(7), "getDigit(7)");
        assertEquals(0, Main.getDigit(0), "getDigit(0)");
        assertEquals(3, Main.getDigit(12), "getDigit(12)");
        assertEquals(9, Main.getDigit(18), "getDigit(18)");
        assertEquals(1, Main.getDigit(10), "getDigit(10)");
    }

    @Test
    void getSize() {
        assertEquals(1, Main.getSize(7), "getSize(7)");
        assertEquals(4, Main.getSize(4388), "getSize(4388)");
        assertEquals(16, Main.getSize(4388576018410707L), "getSize(4388576018410707L)");
    }

    @Test
    void getPrefix() {
        assertEquals(43, Main.getPrefix(4388576018410707L, 2), "getPrefix(4388576018410707L, 2)");
        assertEquals(4, Main.getPrefix(4388576018410707L, 1), "getPrefix(4388576018410707L, 1)");
        assertEquals(123, Main.getPrefix(123, 5), "getPrefix(123, 5): fewer than k digits returns the number");
    }

    @Test
    void prefixMatched() {
        assertTrue(Main.prefixMatched(4388576018410707L, 4), "4388... starts with 4");
        assertFalse(Main.prefixMatched(4388576018410707L, 5), "4388... does not start with 5");
        assertTrue(Main.prefixMatched(378282246310005L, 37), "3782... starts with 37");
        assertFalse(Main.prefixMatched(348282246310005L, 37), "3482... does not start with 37");
    }

    @Test
    void sumOfDoubleEvenPlace() {
        assertEquals(37, Main.sumOfDoubleEvenPlace(4388576018402626L), "sumOfDoubleEvenPlace(4388576018402626L)");
        assertEquals(29, Main.sumOfDoubleEvenPlace(4388576018410707L), "sumOfDoubleEvenPlace(4388576018410707L)");
    }

    @Test
    void sumOfOddPlace() {
        assertEquals(38, Main.sumOfOddPlace(4388576018402626L), "sumOfOddPlace(4388576018402626L)");
        assertEquals(41, Main.sumOfOddPlace(4388576018410707L), "sumOfOddPlace(4388576018410707L)");
    }

    @ParameterizedTest(name = "{0} is valid")
    @ValueSource(longs = {4388576018410707L, 4111111111111111L, 378282246310005L, 6011111111111117L, 5555555555554444L})
    void validCards(long number) {
        assertTrue(Main.isValid(number), number + " should be valid");
    }

    @ParameterizedTest(name = "{0} is invalid")
    @ValueSource(longs = {
        4388576018402626L,   // fails the Luhn check
        1234567812345670L,   // passes Luhn, but 1 is not a valid prefix
        4111L,               // too short
        41111111111111111L,  // too long (17 digits)
    })
    void invalidCards(long number) {
        assertFalse(Main.isValid(number), number + " should be invalid");
    }

    @Test
    void mainReportsValid() {
        String out = TestUtil.runMain(Main.class, "4388576018410707\n");
        assertTrue(out.contains("4388576018410707 is valid"), "Expected \"4388576018410707 is valid\" in:\n" + out);
    }

    @Test
    void mainReportsInvalid() {
        String out = TestUtil.runMain(Main.class, "4388576018402626\n");
        assertTrue(out.contains("4388576018402626 is invalid"), "Expected \"4388576018402626 is invalid\" in:\n" + out);
    }
}
