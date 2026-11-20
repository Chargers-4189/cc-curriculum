import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(4);
        nums.add(-2);
        nums.add(-7);
        nums.add(5);
        nums.add(-1);
        nums.add(8);

        System.out.println("Before: " + nums);
        removeNegatives(nums);
        System.out.println("After: " + nums);
    }

    // Remove every number less than 0 from the list.
    public static void removeNegatives(ArrayList<Integer> list) {

    }
}
