public class P04_largest_palindrome {
    static boolean isPalin (long num) {
        String s = String.valueOf(num);
        int n = s.length();
        for (int i = 0; i < (n/2); i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) 
                return false;
        }
        return true;
    }

    public static void main (String[] args) {
        long curr_large = 1;
        for (int i = 900; i < 1000; i++) {
            for (int j = 900; j < 1000; j++) {
                long prod = i * j;
                if (prod > curr_large && isPalin(prod))
                    curr_large = prod;
            }
        }
        System.out.println ("Largest palindrome is :" + curr_large);
    }
}
