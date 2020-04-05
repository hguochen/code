interface SomeFunc<T> {
    T func(T t);
}

class GenericFunctionalInterfaceDemo {
    public static void main(String[] args) {
        // Use a string based version of SomeFunc
        SomeFunc<String> reverse = (str) -> {
            String result = "";
            int i;

            for (i = str.length()-1; i >= 0; i--) {
                result += str.charAt(i);
            }
            return result;
        };

        System.out.println("Lambda reversed is " + reverse.func("Lambda"));
        System.out.println("Expression reversed is " + reverse.func("Expression"));

        // Now, use an Integer ased version of SomeFunc
        SomeFunc<Integer> factorial = (n) -> {
            int result = 1;
            for (int i=1; i <= n; i++) {
                result = i * result;
            }
            return result;
        };

        System.out.println("The factoail of 3 is " + factorial.func(3));
        System.out.println("The factoail of 5 is " + factorial.func(5));
    }
}