public class Main {
    public static void main(String[] args) {
        // Six matches on the schedule. Matches that haven't been played yet are null.
        Match[] schedule = new Match[6];
        schedule[0] = new Match(1, 85, 72);
        schedule[1] = new Match(2, 64, 90);
        schedule[2] = new Match(3, 101, 98);
        schedule[3] = new Match(4, 77, 80);

        System.out.println("Played: " + countPlayed(schedule));
        System.out.println("Red won: " + redWins(schedule));
        Match best = highestScoring(schedule);
        System.out.println("Highest scoring: match " + best.getNumber());

        // The refs add a penalty against blue in match 4
        schedule[3].addPenalty("blue", 5);
        System.out.println("Red won: " + redWins(schedule));
    }

    // Write countPlayed, redWins and highestScoring here.

}

// Match is done. Don't change it.
class Match {
    private int number;
    private int redScore;
    private int blueScore;

    public Match(int number, int redScore, int blueScore) {
        this.number = number;
        this.redScore = redScore;
        this.blueScore = blueScore;
    }

    public int getNumber() {
        return number;
    }

    public int getRedScore() {
        return redScore;
    }

    public int getBlueScore() {
        return blueScore;
    }

    public void addPenalty(String alliance, int points) {
        // A penalty gives points to the other alliance
        if (alliance.equals("red")) {
            blueScore += points;
        } else {
            redScore += points;
        }
    }
}
