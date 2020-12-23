import java.util.*;

class TreeMapDemo {
    public static void main(String[] args) {
        TreeMap<String, Double> tm = new TreeMap<String, Double>();

        tm.put("John", new Double(35.57));
        tm.put("Tom", new Double(37.68));
        tm.put("Jane", new Double(630.47));
        tm.put("Ralph", new Double(5827.75));

        // get a set of the entries
        Set<Map.Entry<String, Double>> set = tm.entrySet();

        //display the elements
        for (Map.Entry<String, Double> me : set) {
            System.out.println(me.getKey() + ": " + me.getValue());
        }
        System.out.println();

        // deposit 100 into John's account
        double balance = tm.get("John");
        tm.put("John", balance + 1000);

        System.out.println("John's new balance " + tm.get("John"));
    }
}