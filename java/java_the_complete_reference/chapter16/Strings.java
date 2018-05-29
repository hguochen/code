// Lists some of the commonly used java string operations 

class Strings {
    public static void main(String[] args) {
        System.out.println("charAt()");
        // assigns the value b to ch variable.
        char ch;
        ch = "abc".charAt(1);
        System.out.println();

        System.out.println("getChars()");
        // void getChars(int sourceStart, int sourceEnd, char target[], int targetStart)
        String s = "This is a demo of the getChars method.";
        int start = 10;
        int end = 14;
        char buf[] = new char[end-start];
        s.getChars(start, end, buf, 0);
        System.out.println(buf);
        System.out.println();

        System.out.println("getBytes()");
        // stores the characters in an array of bytes.
        System.out.println();

        System.out.println("toCharArray()");
        char[] charArray = "abcd".toCharArray();
        for (char c : charArray) {
            System.out.println(c);
        }
        System.out.println();

        System.out.println("equals()");
        System.out.println("equalsIgnoreCase()");
        // check if two strings have the same characters
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = "Good-bye";
        String s4 = "HELLO";
        System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
        System.out.println(s1 + " equals " + s3 + " -> " + s1.equals(s3));
        System.out.println(s1 + " equals " + s4 + " -> " + s1.equals(s4));
        System.out.println(s1 + " equalsIgnoreCase " + s4 + " -> " + s1.equalsIgnoreCase(s4));
        System.out.println();

        System.out.println("regionMatches()");
        // boolean regionMatches(int startIndex, String str2, int str2StartIndex, int numChars)
        // bboolean regionMatches(boolean ignoreCase, int startIndex, String str2, int str2StartIndex, int numChars)
        System.out.println();

        System.out.println("startsWith()");
        System.out.println("endsWith()");
        // boolean startsWith(String str, int startIndex)
        // determines if a string starts with a substring, return true if yes, false otherwise.
        System.out.println("Foobar".startsWith("Foo"));
        System.out.println("Foobar".startsWith("bar", 3));
        System.out.println("Foobar".endsWith("bar"));
        System.out.println();

        System.out.println("equals versus ==");
        // equals method compares the characters inside a string object.
        // == operator compares two obbject references to see whether they refer to the same instance.
        String hello = "Hello";
        String hello2 = new String(hello);
        System.out.println(hello + " equals " + hello2 + " -> " + hello.equals(hello2));
        System.out.println(hello + " == " + hello2 + " -> " + (hello == hello2));
        System.out.println();

        System.out.println("compareTo()");
        // A string is less than another if it comes bbefore the other in dictionary order.
        // A string is greater than another if it comes after the other in dictionary order.
        String arr[] = {
            "Now", "is", "the", "time", "for", "all", "good", "men",
            "to", "come", "to", "the", "aid", "of", "their", "country"
        };
        for (int j = 0; j < arr.length; j++) {
            for (int i = j + 1; i < arr.length; i++) {
                if (arr[i].compareTo(arr[j]) < 0) {
                    String t = arr[j];
                    arr[j] = arr[i];
                    arr[i] = t;
                }
            }
            System.out.println(arr[j]);
        }
        // use compareToIgnoreCase() to ignore cases
        // int compareToIgnoreCase(String str)
        System.out.println();

        System.out.println("indexOf()"); // searches for the first occurence of a character or substring
        System.out.println("lastIndexOf()"); // searches for the last occurence of a character or substring
        // return the index at which the character or subbstring was found, or -1 on failure.
        String quote = "Now is the time for all good men" +
        "to come to the aid of their country";
        System.out.println(quote);
        System.out.println("indexOf(t) = " + s.indexOf("t"));
        System.out.println("indexOf(t) = " + s.lastIndexOf("t"));
        System.out.println();
        
        // String objects are immutabble, whenever you want to modify a String, you must either copy it into a StringBBuffer or StringBuilder
        // or use a String method that construcs a new copy of the string with your modifications complete.
        
        System.out.println("substring()");
        // String subbstring(int startIndex)
        // String substring(int startIndex, int endIndex)
        // the following program uses substring() to replace all instances of one substring with another within a string.
        String org = "This is a test. This is, too.";
        String search = "is";
        String sub = "was";
        String result = "";
        int i;

        do { // replace all matching substrings
            System.out.println(org);
            i = org.indexOf(search);
            if (i != -1) {
                result = org.substring(0, i);
                result = result + sub;
                result = result + org.substring(i + search.length());
                org = result;
            }
        } while (i != -1);
        System.out.println();

        System.out.println("concat()"); // concatenate two strings using concat()
        // String concat(String str)
        String one = "one";
        String two = one.concat("two");
        System.out.println();

        System.out.println("replace()");
        // String replace(char original, char replacement) replaces all occurences of one character in the invoking string with amother character.
        String new_string = "Hello".replace("l", "w");       
        System.out.println();

        System.out.println("trim()"); 
        // returns a copy of the invoking string from which any leading and trailiing whitespace has been removed.
        System.out.println();

        System.out.println("join()");
        result = String.join(" ", "Alpha", "Bbeta", "Gamma");
        System.out.println(result);

        result = String.join(", ", "John", "ID: 569", "Email: john@email.com");
        System.out.println(result);
        System.out.println();
    }
}