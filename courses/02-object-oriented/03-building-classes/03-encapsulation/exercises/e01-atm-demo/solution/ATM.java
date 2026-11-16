public class ATM {
    // --- Hiding the Data ---
    // private: only code inside ATM can touch these
    private int balance;
    private String name;

    public ATM(String newName, int newBalance) {
        name = newName;
        balance = newBalance;
    }

    // --- Setters Can Say No ---
    // Check the amount before changing the balance
    public int deposit(int amount) {
        if (amount > 0) {
            balance = balance + amount;
        }
        return balance;
    }

    public int withdraw(int amount) {
        if (amount > 0 && amount <= balance) {
            balance = balance - amount;
        }
        return balance;
    }

    // --- Read-Only ---
    // Getters but no setters: you can see the name and balance, but not set them
    public String getName() {
        return name;
    }

    public int getBalance() {
        return balance;
    }
}
