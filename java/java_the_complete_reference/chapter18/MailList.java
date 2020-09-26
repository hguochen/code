import java.util.*;

class Address {
    private String name;
    private String street;
    private String city;
    private String state;
    private String code;

    Address(String n, String s, String c, String st, String cd) {
        name = n;
        street = s;
        city = c;
        state = st;
        code = cd;
    }

    public String toString() {
        return name + "\n" + street + "\n" + city + " " + state + " " + code;
    }
}

class MailList {
    public static void main(String[] args) {
        LinkedList<Address> ml = new LinkedList<Address>();

        ml.add(new Address("name1", "street1", "city1", "state1", "code1"));
        ml.add(new Address("name2", "street2", "city2", "state2", "code2"));
        ml.add(new Address("name3", "street3", "city3", "state3", "code3"));
        ml.add(new Address("name4", "street4", "city4", "state4", "code4"));
        ml.add(new Address("name5", "street5", "city5", "state5", "code5"));

        for(Address element : ml) {
            System.out.println(element + "\n");
        }
        System.out.println();
    }
}