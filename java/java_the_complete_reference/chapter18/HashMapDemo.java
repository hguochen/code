import java.util.*;

class HashMapDemo {
    public static void main(String[] args) {
        // create a hash map
        HashMap<String, Double> hm = new HashMap<String, Double>();

        // put elements to the map
        hm.put("John Doe", new Double(34.64));
        hm.put("Gary", new Double(6438.43));
        hm.put("Josephine", new Double(38.67));
        hm.put("Valerie", new Double(37.97));
        hm.put("Tom", new Double(947.27));

        // get a set of the entries
        Set<Map.Entry<String, Double>> set = hm.entrySet();

        // Display the set
        for (Map.Entry<String, Double> me : set) {
            System.out.println(me.getKey() + ": " + me.getValue());
        }

        System.out.println();

        double balance = hm.get("John Doe");
        hm.put("John Doe", balance + 1000);

        System.out.println("John Doe's new balance: " + hm.get("John Doe"));
    }
}