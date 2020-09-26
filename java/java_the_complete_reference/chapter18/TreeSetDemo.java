import java.util.TreeSet;

class TreeSetDemo {
    public static void main(String[] args) {
        TreeSet<Integer> ts = new TreeSet<Integer>();

        ts.add(5);
        ts.add(39);
        ts.add(38);
        ts.add(9);
        ts.add(1);
        ts.add(86);

        System.out.println(ts);

        ts.remove(38);
        System.out.println(ts);
    }
}