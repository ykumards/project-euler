# include <iostream>
# include <math.h>

/*
Problem 3::

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

using namespace std;

int findLargestPrime(long int n) {
  int max_prime = 1;
  int i = 1;
  while (n != 1) {
    if (n % i == 0) {
      n = n / i;
      max_prime = i;
    }
    i++;
  }
  return max_prime;
}

int main(void){
    
    int i = 1;
    long int n = 600851475143;
    cout << "Largest Prime for " << n << " is: " << findLargestPrime(n) << endl;
    return 0;
}
