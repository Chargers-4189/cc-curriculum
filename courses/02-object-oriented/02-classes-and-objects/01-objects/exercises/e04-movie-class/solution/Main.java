public class Main {
    public static void main(String[] args) {
        Movie first = new Movie();
        first.title = "Iron Lung";
        first.genre = "Horror";
        first.rating = 9;
        first.playIt();

        Movie second = new Movie();
        second.title = "Toy Story 5";
        second.genre = "Comedy";
        second.rating = 7;
        second.playIt();

        System.out.println(first.title + " is rated " + first.rating);
        System.out.println(second.title + " is a " + second.genre + " movie");
    }
}

// Write the Movie class here.
class Movie {
    // What a Movie knows: title (String), genre (String), rating (int)
    String title;
    String genre;
    int rating;

    // What a Movie does: playIt()
    void playIt() {
        System.out.println("Playing the movie " + title);
    }
}
