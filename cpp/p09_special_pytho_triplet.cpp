/*

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
*/

#include<iostream>

using namespace std;

int main()
{
  long prod;
  for (int a = 1; a <= 1000; a++)
  {
    for (int b = a; b < (1000 - a); b++)
    {
      int c = 1000 - b - a;
      if (a*a + b*b == c*c){
        prod = a * b * c;
        break;
      }
    }
  }
  cout << "Product of Pythogorean triplet is: " << prod << endl;
}
