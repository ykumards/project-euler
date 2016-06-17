/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(int n)
{
  if (n == 1) 
    return false;
  if (n == 2)
    return true;
  if (n % 2 == 0)
    return false;
  long ilimit = ceil(sqrt(n));
  for (int i = 3; i < ilimit+1; i++)
  {
    if (n % i == 0)
      return false;
  }
  return true;
}

int main()
{
  int primeCount = 0;
  long n = 1;
  while (primeCount < 10001)
  {
    n++;
    if (isPrime(n))
      primeCount++;
  }
  cout << "10001th prime number is: " << n << endl;
  return 0;
}
