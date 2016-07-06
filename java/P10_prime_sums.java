/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution: 142913828922
*/


public class P10_prime_sums {
	// Function returns true is n is prime and false otherwise
	public static boolean isPrime (int n) {
		if (n < 2)
			return false;
		else if (n == 2)
			return true;
		else if (n % 2 == 0)
			return false;
		else {
			int n_limit = (int) Math.ceil(Math.sqrt(n));
			for (int i = 3; i < n_limit+1; i++) {
				if (n % i == 0)
					return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		long limit = 2000000;
		long prime_sum = 0;
		for (int i = 2; i <= limit; i++) {
			if (isPrime(i))
				prime_sum += i;
		}
		System.out.println("Sum of Primes under 2 Million is: " + prime_sum);
	}
}