// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("Valid Visa")
    void case1() {
        TestUtil.assertOutput(Main.class, "4388576018410707\n", "Enter a credit card number as a long integer: 4388576018410707 is valid");
    }

    @Test
    @DisplayName("Fails the Luhn check")
    void case2() {
        TestUtil.assertOutput(Main.class, "4388576018402626\n", "Enter a credit card number as a long integer: 4388576018402626 is invalid");
    }

    @Test
    @DisplayName("Valid Amex (15 digits)")
    void case3() {
        TestUtil.assertOutput(Main.class, "378282246310005\n", "Enter a credit card number as a long integer: 378282246310005 is valid");
    }

    @Test
    @DisplayName("Valid Discover")
    void case4() {
        TestUtil.assertOutput(Main.class, "6011111111111117\n", "Enter a credit card number as a long integer: 6011111111111117 is valid");
    }

    @Test
    @DisplayName("Bad prefix")
    void case5() {
        TestUtil.assertOutput(Main.class, "1234567812345670\n", "Enter a credit card number as a long integer: 1234567812345670 is invalid");
    }

    @Test
    @DisplayName("Too short")
    void case6() {
        TestUtil.assertOutput(Main.class, "4111\n", "Enter a credit card number as a long integer: 4111 is invalid");
    }
}
