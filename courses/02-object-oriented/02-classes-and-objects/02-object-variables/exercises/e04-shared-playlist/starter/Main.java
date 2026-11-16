public class Main {
    public static void main(String[] args) {
        // Print each playlist like this:
        // System.out.println(roadTrip.name + ": " + roadTrip.songCount + " songs");

        // Part 1


        // Part 2

    }
}

// The Playlist class is done. Don't change it.
class Playlist {
    String name;
    int songCount;

    Playlist(String name) {
        this.name = name;
    }

    void addSong() {
        songCount++;
    }
}
