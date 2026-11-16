public class Main {
    public static void main(String[] args) {
        Stock oracle = new Stock("ORCL", "Oracle Corporation");
        oracle.previousClosingPrice = 34.5;
        oracle.currentPrice = 34.35;

        Stock apple = new Stock("AAPL", "Apple Inc.", 200);
        apple.currentPrice = 210;

        System.out.printf("%s (%s): %.2f%%%n", oracle.name, oracle.symbol, oracle.getChangePercent());
        System.out.printf("%s (%s): %.2f%%%n", apple.name, apple.symbol, apple.getChangePercent());
    }
}

class Stock {
    // Write the Stock class here.
    String symbol;
    String name;
    double previousClosingPrice;
    double currentPrice;

    public Stock(String symbol, String name) {
        this.symbol = symbol;
        this.name = name;
    }

    public Stock(String symbol, String name, double previousClosingPrice) {
        this.symbol = symbol;
        this.name = name;
        this.previousClosingPrice = previousClosingPrice;
    }

    double getChangePercent() {
        return (currentPrice - previousClosingPrice) / previousClosingPrice * 100;
    }
}
