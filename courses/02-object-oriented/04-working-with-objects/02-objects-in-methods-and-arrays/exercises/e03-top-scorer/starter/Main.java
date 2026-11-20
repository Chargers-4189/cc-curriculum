public class Main {
    public static void main(String[] args) {
        Player[] players = {
            new Player("Quinn", 12),
            new Player("Caleb", 27),
            new Player("Bryan", 19),
            new Player("Avery", 27)
        };

        Player best = topScorer(players);
        System.out.println("Top scorer: " + best.getName() + " with " + best.getPoints());
        System.out.println("Team total: " + totalPoints(players));
    }

    // topScorer: give back the Player with the most points (the first one if there's a tie)

    // totalPoints: give back everyone's points added up
}

// Player is done. Don't change it.
class Player {
    private String name;
    private int points;

    public Player(String name, int points) {
        this.name = name;
        this.points = points;
    }

    public String getName() {
        return name;
    }

    public int getPoints() {
        return points;
    }
}
