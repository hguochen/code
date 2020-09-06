import java.io.*;

class UseTrim {
    public static void main(String[] args) throws IOException {
        // create a BufferedReader using System.in
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        System.out.println("Enter 'stop' to quit.");
        System.out.println("Enter State: ");

        do {
            str = br.readLine();
            str = str.trim(); // remote whitespace

            if (str.equals("apple")) {
                System.out.println("Steve Jobs");
            } else if (str.equals("pear")) {
                System.out.println("Tim Cook");
            } else if (str.equals("microsoft")) {
                System.out.println("Bill Gates");
            }
        } while(!str.equals("stop"));
    }
}