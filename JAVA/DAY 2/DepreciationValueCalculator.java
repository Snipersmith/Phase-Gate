public class DepreciationValueCalculator {

    public static int calculateYears(double price) {
        double rate = 0.08;
        int years = 0;

        while (price > 0) {
            double loss = price * rate;
            price = price - loss;
            years = years + 1;
        }

        return years;
    }

    public static void main(String[] args) {
        int numberOfItems = 2;
        double price = 50000;

        for (int index = 1; index <= numberOfItems; index++) {
            int years = calculateYears(price);
            System.out.println("Item " + index + ": It will take " + years + " years to get this for free.");
        }
    }
}


