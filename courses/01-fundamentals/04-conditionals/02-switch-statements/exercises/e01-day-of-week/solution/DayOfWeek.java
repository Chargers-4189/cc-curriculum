import java.util.Scanner;

public class DayOfWeek {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // 1. Prompt for the year, month, and day of the month
        System.out.print("Enter year: (e.g., 2012): ");
        int year = input.nextInt();
        System.out.print("Enter month: 1-12: ");
        int month = input.nextInt();
        System.out.print("Enter the day of the month: 1-31: ");
        int q = input.nextInt();

        // 2. Adjust January and February (months 13 and 14 of the previous year)
        if (month == 1 || month == 2) {
            month += 12;
            year--;
        }

        // 3. Calculate j, k, and h with Zeller's congruence
        int j = year / 100;
        int k = year % 100;
        int h = (q + 26 * (month + 1) / 10 + k + k / 4 + j / 4 + 5 * j) % 7;

        // 4. Use a switch to print "Day of the week is <Day>"
        String day;
        switch (h) {
            case 0:
                day = "Saturday";
                break;
            case 1:
                day = "Sunday";
                break;
            case 2:
                day = "Monday";
                break;
            case 3:
                day = "Tuesday";
                break;
            case 4:
                day = "Wednesday";
                break;
            case 5:
                day = "Thursday";
                break;
            default:
                day = "Friday";
        }
        System.out.println("Day of the week is " + day);
    }
}
