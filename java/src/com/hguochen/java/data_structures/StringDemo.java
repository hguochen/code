package com.hguochen.java.data_structures;

import java.lang.String;
import java.util.Arrays;

// java.lang.String demo
public class StringDemo {
    public static void main(String[] args) {
        // default way to initialize string
        String str1 = "hello world. this is a test string!";

        // returns the char value at the specified index.
        System.out.println(str1.charAt(0)); // h

        // returns the character unicode point at the specified index
        System.out.println("a".codePointAt(0)); // 97

        // returns the character unicode point before the specified index
        System.out.println("ab".codePointBefore(1)); // 97

        // returns the number of unicode code points in the specified test range
        System.out.println("--------------codPointCount-----------------");
        System.out.println("abcd".codePointCount(0, 2)); // 2
        // compares two strings lexicographically
        // comparison based on the unicode value of each char in string
        // results negative int if this string object comes before the argument string. the int is the space apart
        System.out.println("--------------compareTo-----------------");
        System.out.println("a".compareTo("c")); // -2
        // results positive int if this string object comes after the argument string.
        System.out.println("d".compareTo("c")); // 1
        // results is 0 if the strings are equal
        System.out.println("a".compareTo("a")); // 0

        // concatenates the specified string to the end of this string
        System.out.println("--------------compareTo-----------------");
        System.out.println("hello ".concat("world!")); // hello world

        // returns true if and only if this string contains the specified sequence of char values
        System.out.println("--------------contains-----------------");
        System.out.println("hello world".contains("hello")); // true
        System.out.println("hello world".contains("gary")); // false

        // test if this string ends with the specified index
        System.out.println("--------------endsWith-----------------");
        System.out.println("hello world".endsWith("orld")); // true
        System.out.println("hello world".endsWith("gary")); // false

        // compares this string ot the specified object
        System.out.println("--------------equals-----------------");
        System.out.println("hello".equals("hello")); // true
        System.out.println("hello".equals("world")); // false

        // compares this string to another string, ignoring case considerations
        System.out.println("--------------equalsIgnoreCase-----------------");
        System.out.println("hello".equalsIgnoreCase("HeLLo")); // true
        System.out.println("hello".equalsIgnoreCase("wOrLD")); // false

        // returns the index within this string of the first occurrence of the specified character
        System.out.println("--------------indexOf-----------------");
        System.out.println("hello".indexOf("o")); // 4
        // starting at the specified index
        System.out.println("hello".indexOf("l", 2)); // 2
        System.out.println("hello".indexOf("l", 3)); // 3
        System.out.println("hello".indexOf("l", 4)); // -1

        //returns true if and only if length is 0
        System.out.println("--------------isEmpty-----------------");
        System.out.println("".isEmpty()); // true
        System.out.println("hello".isEmpty()); // false

        // returns length of the string
        System.out.println("--------------length------------------");
        System.out.println("hello".length()); // 5

        // returns a new string resulting from replacing all occurrences of oldChar with newChar
        System.out.println("--------------replace------------------");
        System.out.println("hello".replace("l", "p")); // heppo

        // splits this string around matches of the given regex
        System.out.println("--------------split------------------");
        String[] strArray = "hello,world".split(",");
        System.out.println(Arrays.toString(strArray)); //["hello", "world]

        // returns a copy of the string with leading and trailing whitespace omitted
        System.out.println("--------------trim------------------");
        System.out.println("      hello world         ".trim()); // "hello world

        // converts all chars to uppercase
        System.out.println("--------------toUpperCase------------------");
        System.out.println("hello world".toUpperCase()); // HELLO WORLD
        // converts all chars to lowercase
        System.out.println("--------------toLowerCase------------------");
        System.out.println("HELLO WORLD".toLowerCase()); // hello world
    }
}
