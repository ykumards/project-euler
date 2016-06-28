public class P03_prime_factors {

   static int findLargestPrime (long n) {
        int max_prime = 1;
        int i = 1;
        while (n != 1) {
            if (n % i == 0) {
                n = n/i;
                max_prime = i;
            }
            i++;
        }
        return max_prime;
    }

    public static void main (String[] args) {
        long n = 600851475143L;
        System.out.println ("Max prime is: " + findLargestPrime(n));
    }
}
