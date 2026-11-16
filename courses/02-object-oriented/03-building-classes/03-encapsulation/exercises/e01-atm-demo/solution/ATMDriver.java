public class ATMDriver {
    public static void main(String[] args) {
        ATM quinnAccount = new ATM("Quinn", 0);

        // --- The Problem ---
        // Before encapsulation, all of this worked:
        // quinnAccount.withdraw(-200);        // a negative withdraw adds money!
        // quinnAccount.balance = 1000000;     // or just set the balance

        // --- Hiding the Data ---
        // quinnAccount.balance = 1000000;     // won't compile now: balance is private

        // --- Setters Can Say No ---
        quinnAccount.deposit(10);
        quinnAccount.withdraw(-100);   // ignored
        quinnAccount.withdraw(50);     // ignored, there's only 10
        System.out.println(quinnAccount.getBalance());   // 10

        // --- Read-Only ---
        System.out.println(quinnAccount.getName() + " has $" + quinnAccount.getBalance());
    }
}
