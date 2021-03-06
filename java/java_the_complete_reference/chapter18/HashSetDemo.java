import java.util.*;

class HashSetDemo {
    public static void main(String[] args) {
        HashSet<String> hs = new HashSet<String>();

        // add elements to hashset
        hs.add("Beta");
        hs.add("Alpha");
        hs.add("Eta");
        hs.add("Gamma");
        hs.add("Epsilon");
        hs.add("Omega");
        hs.add("Omega");

        System.out.println(hs);

        ArrayList<String> al = new ArrayList<String>();
        al.add("Apple");
        al.add("Pear");
        al.add("Guava");
        HashSet<String> hs2 = new HashSet<String>(al);

        System.out.println(hs2);
    }
}