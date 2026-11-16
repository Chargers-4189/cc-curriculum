public class Main {
    public static void main(String[] args) {
        Cat tom = new Cat();
        tom.setHeight(27);
        System.out.println("Height: " + tom.getHeight());
        tom.setHeight(0);
        System.out.println("Height: " + tom.getHeight());
        tom.setHeight(12);
        System.out.println("Height: " + tom.getHeight());
    }
}

class Cat {
    private int height;

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        if (height > 9) {
            this.height = height;
        }
    }
}
