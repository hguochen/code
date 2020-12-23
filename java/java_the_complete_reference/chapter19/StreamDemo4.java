import java.util.*;
import java.util.stream.*;

class StreamDemo4 {
    public static void main(String[] args) {
        ArrayList<Double> myList = new ArrayList<>();

        myList.add(7.0);
        myList.add(18.0);
        myList.add(10.0);
        myList.add(24.0);
        myList.add(17.0);
        myList.add(5.0);

        // map the sqrt of the elements in myList to a new stream
        Stream<Double> sqrtRootStrm = myList.stream().map((a) -> Math.sqrt(a));

        // find product of the sqrts
        double productOfSqrRoots = sqrtRootStrm.reduce(1.0, (a, b) -> a * b);

        System.out.println("Product of square roots is " + productOfSqrRoots);
    }
}