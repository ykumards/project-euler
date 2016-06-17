/*
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

#include <iostream>
#include <cmath>

using namespace std;

long sum_of_squares(int n)
{
  return (n * (n + 1) * (2*n + 1))/6;
}

long square_of_sums(int n)
{
  return pow(((n * (n + 1)) * 0.5), 2);
}

int main()
{
  int n = 100;
  cout << "Solution: " << (square_of_sums(n) - sum_of_squares(n)) << endl;
  return 0;
}
