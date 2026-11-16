public class TeamA {
    public static final int SQUARE = 1;
    public static final int CIRCLE = 2;
    public static final int TRIANGLE = 3;
    public static final int AMOEBA = 4;

    public static void main(String[] args) {
        // Pretend the user clicked these shapes, in this order.
        int[] clicks = { SQUARE, CIRCLE, TRIANGLE, AMOEBA };

        for (int shapeNum : clicks) {
            handleClick(shapeNum);
        }
    }

    public static void handleClick(int shapeNum) {
        System.out.println("--- user clicked the " + getName(shapeNum) + " ---");
        rotate(shapeNum);
        playSound(shapeNum);
        System.out.println();
    }

    public static String getName(int shapeNum) {
        switch (shapeNum) {
            case SQUARE:   return "square";
            case CIRCLE:   return "circle";
            case TRIANGLE: return "triangle";
            case AMOEBA:   return "amoeba";
            default:       return "unknown shape";
        }
    }

    public static double getWidth(int shapeNum) {
        switch (shapeNum) {
            case SQUARE:   return 50;
            case CIRCLE:   return 40;
            case TRIANGLE: return 60;
            case AMOEBA:   return 35;
            default:       return 0;
        }
    }

    public static double getHeight(int shapeNum) {
        switch (shapeNum) {
            case SQUARE:   return 50;
            case CIRCLE:   return 40;
            case TRIANGLE: return 30;
            case AMOEBA:   return 20;
            default:       return 0;
        }
    }

    /** Every shape spins around the center of the box that surrounds it (except the amoeba). */
    public static void rotate(int shapeNum) {
        double centerX = getWidth(shapeNum) / 2;
        double centerY = getHeight(shapeNum) / 2;
        if (shapeNum == AMOEBA) {
            centerX = 0;
            centerY = 10;
        }
        System.out.println("Rotating the " + getName(shapeNum)
                + " 360 degrees around (" + centerX + ", " + centerY + ")");
    }

    public static void playSound(int shapeNum) {
        switch (shapeNum) {
            case SQUARE:
                System.out.println("Playing square.wav");
                break;
            case CIRCLE:
                System.out.println("Playing circle.wav");
                break;
            case TRIANGLE:
                System.out.println("Playing triangle.wav");
                break;
            case AMOEBA:
                System.out.println("Playing amoeba.mp3");
                break;
            default:
                System.out.println("No sound for this shape");
        }
    }

}
