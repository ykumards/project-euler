public class P01_multiples {
    public static void main (String[] args) {
        int result_sum = 0;
        int iter_limit = 1000;
        for (int i=3; i < iter_limit; i++) {
            if ((i % 3 == 0) || (i % 5 == 0))
                result_sum += i;
        }
        System.out.println ("Sum of multiples of 3 or 5 less than 1000 is " + result_sum);
    }
}
