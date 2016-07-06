/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution: 31875000
*/
public class P09_pythagorean_trips {
	public static long getProd() {
		for (int a = 1; a < 1000; a++){
			for (int b = a; b < 1000-a; b++){
				int c = 1000 - b - a;
				if (a*a + b*b == c*c) {
			 		return a * b * c;
			 	}
			}
		}
		return -1;
	}

	public static void main (String[] args) {
		System.out.println("Product of the special triplet is: " + getProd());
	}
}