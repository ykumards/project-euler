import math
'''
Problem finds the 10001th prime number by brute force, it still has
a polynomial complexity so I guess brute force suffices
Alternative is Sieve method, which will also be polynomial
'''

def isPrime(num):
  if num == 1: return False
  if num == 2: return True
  if num % 2 == 0: return False
  ilimit = int(math.floor(math.sqrt(num)))
  for i in xrange(3, ilimit + 1):
    if num % i == 0:
      return False
  return True


def main():
  primeCount = 0
  number = 1
  while primeCount < 10001:
    number += 1
    if isPrime(number):
      primeCount += 1
  print number


if __name__ == '__main__':
  main()
