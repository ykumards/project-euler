/*
Q: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

We need to find the LCM of 20 numbers
*/

#include <iostream>

using namespace std;

// GCD calculation using euclid's algorithm
long gcd(long a, long b)
{
  if (b > a)
    swap(a, b);
  if (b == 0)
    return a;
  int r = a % b;
  return gcd(b, r);
}

// LCM of two numbers a & b is a*b/gcd(a,b)
long lcm(long a, long b)
{
  return (a * b)/gcd(a,b);
}

int main()
{
  long result = 2;
  long x = 3;
  // We now just have to find the LCM by taking two
  // numbers at a time
  while (x <= 20)
  {
    result = lcm(result, x);
    x++;
  }
  cout << "LCM is: " << result << endl;
  return 0;
}
