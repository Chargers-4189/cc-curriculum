// Generated from cases.csv by tools/cases.py. Edit cases.csv, not this file.
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    @DisplayName("The example")
    void case1() {
        TestUtil.assertOutput(Main.class, "add Quinn\nadd Caleb\nadd Quinn\nlist\nremove Bryan\nremove Caleb\ncount\nquit\n", "Added Quinn\nAdded Caleb\nQuinn is already on the team\nTeam: [Quinn, Caleb]\nBryan isn't on the team\nRemoved Caleb\n1 of 4\nBye!");
    }

    @Test
    @DisplayName("Full team")
    void case2() {
        TestUtil.assertOutput(Main.class, "add A\nadd B\nadd C\nadd D\nadd E\ncount\nlist\nquit\n", "Added A\nAdded B\nAdded C\nAdded D\nThe team is full\n4 of 4\nTeam: [A, B, C, D]\nBye!");
    }

    @Test
    @DisplayName("Unknown command")
    void case3() {
        TestUtil.assertOutput(Main.class, "dance\nlist\nquit\n", "Unknown command: dance\nTeam: []\nBye!");
    }

    @Test
    @DisplayName("Remove then add again")
    void case4() {
        TestUtil.assertOutput(Main.class, "add Avery\nremove Avery\nadd Avery\nlist\nquit\n", "Added Avery\nRemoved Avery\nAdded Avery\nTeam: [Avery]\nBye!");
    }
}
