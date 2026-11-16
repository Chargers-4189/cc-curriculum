public class Main {
    public static void main(String[] args) {
        Thermostat home = new Thermostat(72);
        System.out.println(home.getTemperature());

        home.setTemperature(95);
        System.out.println(home.getTemperature());

        home.down();
        home.down();
        System.out.println(home.getTemperature());

        Thermostat cold = new Thermostat(20);
        cold.down();
        System.out.println(cold.getTemperature());
        cold.up();
        System.out.println(cold.getTemperature());
    }
}

class Thermostat {
    // The temperature can only be from 60 to 80.

}
