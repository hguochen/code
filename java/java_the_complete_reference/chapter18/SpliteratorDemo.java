import java.util.*;

class SpliteratorDemo {
        public static void main(String[] args) {
            ArrayList<Double> vals = new ArrayList<>();

            vals.add(1.0);
            vals.add(2.0);
            vals.add(3.0);
            vals.add(4.0);
            vals.add(5.0);

            // use tryAdvance() to display contents of vals
            System.out.println("Contents of vals:\n");
            Spliterator<Double> spltitr = vals.spliterator();
            while(spltitr.tryAdvance((n) -> System.out.println(n)));
            System.out.println();

            // create a new list that contains square roots
            spltitr = vals.spliterator();
            ArrayList<Double> sqrs = new ArrayList<>();
            while(spltitr.tryAdvance((n) -> sqrs.add(Math.sqrt(n))));

            // use forEachRemaining() to display contents of sqrs
            System.out.println("Contents of sqrs:\n");
            spltitr = sqrs.spliterator();
            spltitr.forEachRemaining((n) -> System.out.println(n));
            System.out.println();
        }
}