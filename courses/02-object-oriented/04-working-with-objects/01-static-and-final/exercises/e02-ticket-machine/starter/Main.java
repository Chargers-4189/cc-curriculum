public class Main {
    public static void main(String[] args) {
        System.out.println("Sold so far: " + Ticket.getTicketsSold());

        Ticket first = new Ticket();
        Ticket second = new Ticket();
        Ticket third = new Ticket();

        System.out.println("First ticket: #" + first.getNumber());
        System.out.println("Second ticket: #" + second.getNumber());
        System.out.println("Third ticket: #" + third.getNumber());
        System.out.println("Sold so far: " + Ticket.getTicketsSold());
    }
}

class Ticket {
    // Write the Ticket class here.

}
