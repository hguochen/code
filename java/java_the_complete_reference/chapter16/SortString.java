import java.util.Arrays;

// A bubble sort for strings
class SortString {
    static String[] arr = {
            "Now", "is", "the", "time", "for", "all", "good", "men", "to", "come", "to", "the", "aid", "of", "their",
            "country"
    };

    public static void main(String[] args) {
        for(int j = 0; j < arr.length; j++) {
            for (int i = j + 1; i<arr.length; i++) {
                if (arr[i].compareToIgnoreCase(arr[j]) < 0) {
                    String temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
            System.out.println(arr[j]);
        }
        System.out.println(Arrays.toString(arr));

        System.out.println();

        String test = "abcdefgh";
        System.out.println(test.indexOf("cd"));
        System.out.println(test.concat("garytest"));
        System.out.println(test.replace('a', 'z'));
        System.out.println("hello".replace('l', 'w'));
    }
}