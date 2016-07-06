/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Solution: 104743
*/

public class P07_prime_10001 {
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
		int index = 0;
		int n = 1;
		while (index < 10001) {
			n++;
			if (isPrime(n)) {
				index++;
			}				
		}
		System.out.println("10001th prime is: " + n);
	}
}