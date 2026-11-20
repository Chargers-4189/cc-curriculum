public class ObjectsTester {
    public static void main(String[] args) {
        // --- Passing an Object to a Method ---
        Robot bolt = new Robot("Bolt", 40);
        int amount = 30;
        chargeUp(bolt, amount);
        System.out.println(bolt.getBattery());   // 70: the method changed the robot
        System.out.println(amount);              // 30: amount was only copied

        // --- Changing the Object vs Changing the Variable ---
        replace(bolt);
        System.out.println(bolt.getName());      // still Bolt

        // --- Returning an Object ---
        Robot spare = makeSpare("Volt");
        System.out.println(spare.getName() + " has " + spare.getBattery() + "%");

        // --- Arrays of Objects ---
        Robot[] team = new Robot[3];
        System.out.println(team[0]);             // null: no robots yet
        team[0] = bolt;
        team[1] = spare;
        team[2] = new Robot("Amp", 15);
        System.out.println(team[2].getName());

        // --- Looping Over Objects ---
        int total = 0;
        for (int i = 0; i < team.length; i++) {
            total += team[i].getBattery();
        }
        System.out.println("Average battery: " + total / team.length + "%");

        // Same thing with a for-each loop: we don't need i
        int total2 = 0;
        for (Robot r : team) {
            total2 += r.getBattery();
        }
        System.out.println("Average battery: " + total2 / team.length + "%");
        System.out.println("Lowest battery: " + lowest(team).getName());
    }

    // Write your static methods down here.
    public static void chargeUp(Robot r, int amount) {
        r.charge(amount);
        amount = 0;   // only changes the copy
    }

    public static void replace(Robot r) {
        r = new Robot("Spare", 100);   // r points somewhere new, bolt doesn't
    }

    public static Robot makeSpare(String name) {
        Robot r = new Robot(name, 100);
        return r;
    }

    public static Robot lowest(Robot[] robots) {
        Robot low = robots[0];
        for (int i = 1; i < robots.length; i++) {
            if (robots[i].getBattery() < low.getBattery()) {
                low = robots[i];
            }
        }
        return low;
    }
}
