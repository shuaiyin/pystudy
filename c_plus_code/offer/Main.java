import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        // String a = "20";
        // boolean rest = a.matches(".*[2-9].*");
        // System.out.print(rest);

        // return 0;
        // Scanner scanner = new Scanner(System.in);
        // int n = scanner.nextInt();

        int n = 10;
        int count = 0;
        for (int i = 1 ; i <= n; i++){
            String str = String.valueOf(i);

            if (!str.matches(".*[2-9].*")){
                count ++;
            }
        }
        System.out.print(count);



    }
}