public class P02_fibo {
    public static void main (String[] args) {
        int current = 1;
        int prev = 0;
        int result_limit = 4000000;
        long result_sum = 0;
        while (current < result_limit) {
            if (current % 2 == 0)
                result_sum += current;
            int temp = current;
            current = temp + prev;
            prev = temp;
        }
        System.out.println("Sum of even Fib numbers less than 4 Mil is: " + result_sum);
    }
}
