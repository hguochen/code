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

        System.out.println(hs);
    }
}