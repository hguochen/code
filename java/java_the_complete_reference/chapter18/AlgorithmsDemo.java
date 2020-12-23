import java.util.*;

class AlgorithmsDemo {
    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.add(-8);
        ll.add(20);
        ll.add(-10);
        ll.add(8);

        //create a reverse order comparator
        Comparator<Integer> r = Collections.reverseOrder();

        Collections.sort(ll, r);

        System.out.println("List sorted in reverse: ");
        for (int i : ll) {
            System.out.print(i + " ");
        }
        System.out.println();
        Collections.shuffle(ll);

        // display randomized list
        System.out.println("List shuffled: ");
        for (int i : ll)
            System.out.print(i + " ");
        System.out.println();

        System.out.println("Minimum: " + Collections.min(ll));
        System.out.println("Maximum: " + Collections.max(ll));
    }
}