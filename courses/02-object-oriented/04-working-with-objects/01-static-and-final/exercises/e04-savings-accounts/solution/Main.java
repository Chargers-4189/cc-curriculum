public class Main {
    public static void main(String[] args) {
        Account.setInterestRate(4.5);

        Account quinn = new Account(20000);
        Account caleb = new Account(1200);
        System.out.println("Account #" + quinn.getId() + ": $" + quinn.getBalance());
        System.out.println("Account #" + caleb.getId() + ": $" + caleb.getBalance());
        System.out.printf("Quinn earns $%.2f a month%n", quinn.getMonthlyInterest());
        System.out.printf("Caleb earns $%.2f a month%n", caleb.getMonthlyInterest());

        // The bank changes the rate for everyone
        Account.setInterestRate(6);
        caleb.deposit(300);
        System.out.println("The rate is now " + Account.getInterestRate() + "%");
        System.out.printf("Quinn earns $%.2f a month%n", quinn.getMonthlyInterest());
        System.out.printf("Caleb earns $%.2f a month%n", caleb.getMonthlyInterest());

        caleb.deposit(-50);   // ignored
        System.out.println("Caleb has $" + caleb.getBalance());
    }
}

class Account {
    // Write the Account class here.
    private static double interestRate = 0;   // yearly, as a percent: 4.5 means 4.5%
    private static int nextId = 1001;

    private final int id;
    private double balance;

    public Account(double balance) {
        this.balance = balance;
        id = nextId;
        nextId++;
    }

    public static void setInterestRate(double rate) {
        interestRate = rate;
    }

    public static double getInterestRate() {
        return interestRate;
    }

    public int getId() {
        return id;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance = balance + amount;
        }
    }

    public double getMonthlyInterest() {
        return balance * interestRate / 100 / 12;
    }
}
