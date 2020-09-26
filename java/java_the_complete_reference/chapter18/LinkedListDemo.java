import java.util.LinkedList;

class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> ll = new LinkedList<String>();

        ll.add("A");
        ll.add("B");
        ll.add("C");
        ll.add("D");
        ll.add("E");
        ll.add("F");
        ll.add(1, "Z");

        System.out.println(ll);

        ll.remove(1);
        System.out.println(ll);

        ll.remove("F");
        System.out.println(ll);

        ll.removeFirst();
        System.out.println(ll);

        ll.removeLast();
        System.out.println(ll);

        String val = ll.get(2);
        ll.set(2, val + " changed");
        System.out.println(ll);
    }
}