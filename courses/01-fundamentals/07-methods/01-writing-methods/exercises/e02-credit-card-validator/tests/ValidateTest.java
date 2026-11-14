import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class ValidateTest {
    @Test
    void getDigit() {
        assertEquals(7, Validate.getDigit(7), "getDigit(7)");
        assertEquals(0, Validate.getDigit(0), "getDigit(0)");
        assertEquals(3, Validate.getDigit(12), "getDigit(12)");
        assertEquals(9, Validate.getDigit(18), "getDigit(18)");
        assertEquals(1, Validate.getDigit(10), "getDigit(10)");
    }

    @Test
    void getSize() {
        assertEquals(1, Validate.getSize(7), "getSize(7)");
        assertEquals(4, Validate.getSize(4388), "getSize(4388)");
        assertEquals(16, Validate.getSize(4388576018410707L), "getSize(4388576018410707L)");
    }

    @Test
    void getPrefix() {
        assertEquals(43, Validate.getPrefix(4388576018410707L, 2), "getPrefix(4388576018410707L, 2)");
        assertEquals(4, Validate.getPrefix(4388576018410707L, 1), "getPrefix(4388576018410707L, 1)");
        assertEquals(123, Validate.getPrefix(123, 5), "getPrefix(123, 5): fewer than k digits returns the number");
    }

    @Test
    void prefixMatched() {
        assertTrue(Validate.prefixMatched(4388576018410707L, 4), "4388... starts with 4");
        assertFalse(Validate.prefixMatched(4388576018410707L, 5), "4388... does not start with 5");
        assertTrue(Validate.prefixMatched(378282246310005L, 37), "3782... starts with 37");
        assertFalse(Validate.prefixMatched(348282246310005L, 37), "3482... does not start with 37");
    }

    @Test
    void sumOfDoubleEvenPlace() {
        assertEquals(37, Validate.sumOfDoubleEvenPlace(4388576018402626L), "sumOfDoubleEvenPlace(4388576018402626L)");
        assertEquals(29, Validate.sumOfDoubleEvenPlace(4388576018410707L), "sumOfDoubleEvenPlace(4388576018410707L)");
    }

    @Test
    void sumOfOddPlace() {
        assertEquals(38, Validate.sumOfOddPlace(4388576018402626L), "sumOfOddPlace(4388576018402626L)");
        assertEquals(41, Validate.sumOfOddPlace(4388576018410707L), "sumOfOddPlace(4388576018410707L)");
    }

    @ParameterizedTest(name = "{0} is valid")
    @ValueSource(longs = {4388576018410707L, 4111111111111111L, 378282246310005L, 6011111111111117L, 5555555555554444L})
    void validCards(long number) {
        assertTrue(Validate.isValid(number), number + " should be valid");
    }

    @ParameterizedTest(name = "{0} is invalid")
    @ValueSource(longs = {
        4388576018402626L,   // fails the Luhn check
        1234567812345670L,   // passes Luhn, but 1 is not a valid prefix
        4111L,               // too short
        41111111111111111L,  // too long (17 digits)
    })
    void invalidCards(long number) {
        assertFalse(Validate.isValid(number), number + " should be invalid");
    }

    @Test
    void mainReportsValid() {
        String out = TestUtil.runMain(Validate.class, "4388576018410707\n");
        assertTrue(out.contains("4388576018410707 is valid"), "Expected \"4388576018410707 is valid\" in:\n" + out);
    }

    @Test
    void mainReportsInvalid() {
        String out = TestUtil.runMain(Validate.class, "4388576018402626\n");
        assertTrue(out.contains("4388576018402626 is invalid"), "Expected \"4388576018402626 is invalid\" in:\n" + out);
    }
}
