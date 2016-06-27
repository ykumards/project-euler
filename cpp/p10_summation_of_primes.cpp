/*

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer : 142913828922
*/

#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

// efficient implementation from algoist.net
vector<int> sieve_maker (const int primes_till) {
  vector<int> primes;
  int sqrt_primes_till = sqrt((double) primes_till);
  vector<bool> isComposite;

  for (int i = 0; i < primes_till; i++)
    isComposite.push_back(false);

  for (int m = 2; m <= sqrt_primes_till; m++) {
    if(!isComposite[m]) {
      primes.push_back(m);
      // Now remove its multiples, we start from its square
      for (int k = m * m; k <= primes_till; k += m) {
        isComposite[k] = true;
      }
    }

    for (int m = sqrt_primes_till; m <= primes_till; m++) {
      if(!isComposite[m])
        primes.push_back(m);
    }
  }
  
  return primes;
}

bool isPrime(int n) {
  
  if (n <= 1) 
    return false;
  if (n == 2)
    return true;
  if(n % 2 == 0)
    return false;
  
  int u_limit = ceil(sqrt(n));

  for (int i = 3; i < u_limit+1; i++) {
    if (n % i == 0)
      return false;
  }

  return true;
}

int main() {
  long primes_till = 2000000;
  long prime_sum = 0;

  for (int i = 2; i <= primes_till; i++) {
    if (isPrime(i))
      prime_sum += i;
  }

  cout << "Sum of primes less than 2 million is: " << prime_sum << endl;
  return 0;
}
