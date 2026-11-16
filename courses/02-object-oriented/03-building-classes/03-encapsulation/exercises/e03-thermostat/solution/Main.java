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
    private int temperature;

    public Thermostat(int temperature) {
        setTemperature(temperature);
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int temperature) {
        if (temperature < 60) {
            this.temperature = 60;
        } else if (temperature > 80) {
            this.temperature = 80;
        } else {
            this.temperature = temperature;
        }
    }

    public void up() {
        setTemperature(temperature + 1);
    }

    public void down() {
        setTemperature(temperature - 1);
    }
}
