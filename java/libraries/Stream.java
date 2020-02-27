import java.util.*;
import java.util.stream.*;

class Person {
    private String name;

    private List<Person> friends = new ArrayList<>();

    Person(String newName) {
        this.name = newName;
    }

    public String getName() {
        return this.name;
    }

    public void addFriend(Person person) {
        this.friends.add(person);
    }

    public List<Person> getFriends() {
        return this.friends;
    }

    public void printFriends() {
        System.out.println(this.friends);
    }
}
public class Stream {
    public static void main(String []args) {
        // Demonstrate use of Stream flatMap
        // set up
        // [Person@7852e922, Person@4e25154f]
        // [Person@70dea4e, Person@5c647e05]
        System.out.println("Hello World");
        Person apple = new Person("apple");
        Person roger = new Person("roger");
        Person pear = new Person("pear");
        Person watermelon = new Person("watermelon");
        Person guave = new Person("guave");
        Person banana = new Person("banana");
        apple.addFriend(roger);
        apple.addFriend(pear);
        watermelon.addFriend(guave);
        watermelon.addFriend(banana);
        apple.printFriends();
        watermelon.printFriends();

        List<Person> family = new ArrayList<>();
        family.add(apple);
        family.add(watermelon);
        System.out.println(family);
        System.out.println("-------------Gary test----------");
        List<List<Person>> familyFriends = family.stream().map(member -> member.getFriends()).collect(Collectors.toList());
        System.out.println(familyFriends);
        System.out.println(
            familyFriends.stream().flatMap(Collection::stream).collect(Collectors.toList())
            );
        System.out.println(
            family.stream().map(member -> member.getFriends()).flatMap(Collection::stream).collect(Collectors.toList())
            );
    }
}