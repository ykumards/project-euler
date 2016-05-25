import sys
import math
'''
Find the largest prime factor of the number 600851475143
'''

def main():
  number = 600851475143
  factor_list = []
  sqrt_number = math.sqrt(number) 
  # Check through each number till sqrt(number)
  # We can ignore all even number since number is not even
  # Runtime will be O(sqrt(n))
  for i in range(3, int(math.floor(sqrt_number))):
    if i % 2 != 0 and number % i == 0:
      factor_list.append(i)

  # First element of the factor list must be prime
  prime_factor_list = []
  prime_factor_list.append(factor_list[0])
  # Loop through factor list to remove composite factors
  for factor in factor_list[1:]:
    isPrime = True
    for prime_factor in prime_factor_list:
      if factor % prime_factor == 0:
        isPrime = False
    if isPrime:
      prime_factor_list.append(factor)
  # Last element in the prime factor list will be the largest
  # prime number
  print prime_factor_list[-1]

if __name__ == '__main__':
  main()
