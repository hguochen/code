class CharDemo {
    public static void main(String args[]) {
        char ch1, ch2;

        ch1 = 88;
        ch2 = 'Y';

        int x = 0b1010; // 10 in binary form
        int y = 123_456_789;
        int z = 0b1101_0101_0001_1010;
        char jap_char = '\ua432';
        String str1 = "hello World two\nlines";

        System.out.println(jap_char);
        System.out.println(str1);
        System.out.println("x is: " + x);
        System.out.println("y is: " + y);
        System.out.println("z is: " + z);
        System.out.print("ch1 and ch2: ");
        System.out.println(ch1 + " " + ch2);
    }
}