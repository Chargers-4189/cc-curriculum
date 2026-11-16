public class ATM {
    // --- The Problem ---
    int balance;
    String name;

    public ATM(String newName, int newBalance) {
        name = newName;
        balance = newBalance;
    }

    // Adds amount to the balance and returns the new balance
    int deposit(int amount) {
        balance = balance + amount;
        return balance;
    }

    // Takes amount out of the balance and returns the new balance
    int withdraw(int amount) {
        balance = balance - amount;
        return balance;
    }

    // --- Hiding the Data ---

    // --- Setters Can Say No ---

    // --- Read-Only ---

}
