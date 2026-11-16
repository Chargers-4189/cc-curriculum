public class Main {
    public static void main(String[] args) {
        // Print each playlist like this:
        // System.out.println(roadTrip.name + ": " + roadTrip.songCount + " songs");

        // Part 1
        Playlist roadTrip = new Playlist("Road Trip");
        Playlist shared = roadTrip;
        shared.addSong();
        shared.addSong();
        roadTrip.addSong();

        Playlist gym = new Playlist("Gym");
        gym.addSong();
        gym.addSong();

        System.out.println(roadTrip.name + ": " + roadTrip.songCount + " songs");
        System.out.println(shared.name + ": " + shared.songCount + " songs");
        System.out.println(gym.name + ": " + gym.songCount + " songs");

        // Part 2
        shared = gym;
        shared.addSong();

        System.out.println(roadTrip.name + ": " + roadTrip.songCount + " songs");
        System.out.println(shared.name + ": " + shared.songCount + " songs");
        System.out.println(gym.name + ": " + gym.songCount + " songs");
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
