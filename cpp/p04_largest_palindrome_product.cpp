/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include <iostream>
#include <string>

using namespace std;

bool isPalin(long int number)
{
  string s = to_string(number);

  // Compare the first half with the second half
  if (equal(s.begin(), s.begin() + s.size()/2, s.rbegin()))
  {
    return true;
  }
  return false;
}

int main() 
{
  long int curr_large = 1;
  // Starting from 999 we can loop downwards
  for (int i = 900; i < 1000; i++)
  {
    for (int j = 900; j < 1000; j++)
    {
      long int prod = i * j;
      if (prod > curr_large && isPalin(prod))
      {
        curr_large = prod;
      }
    }
  }
  cout << "Largest palindrome is: " << curr_large << endl;
  return 0;
}
