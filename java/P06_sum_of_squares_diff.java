/*
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution: 25164150
*/

public class P06_sum_of_squares_diff {
    public static void main (String[] args) {
        int n = 100;
        long sum_of_squares = (n * (n + 1) * (2*n + 1))/6;
        long square_of_sum = (n * (n + 1))/2;
        square_of_sum = (long) Math.pow(square_of_sum, 2);
        long result = square_of_sum - sum_of_squares;
        System.out.println("Solution: " + result);
    }
}
