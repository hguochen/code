import java.util.ArrayList;
import java.util.List;

class ListDemo {
    public static void main(String[] args) {
        List<String> testList = new ArrayList<String>();
        // add elements into list
        testList.add("apple");
        testList.add("pear");
        testList.add(1, "watermelon");
        System.out.println(testList.toString());
        // access specific elements in list
        System.out.println(testList.get(0));
        System.out.println(testList.get(1));
        System.out.println(testList.size());

        testList.remove("pear");
        System.out.println(testList.toString());

        testList.remove(1);
        System.out.println(testList.toString());

        System.out.println(testList.toArray());
    }
}