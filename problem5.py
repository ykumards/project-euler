import math

# Euclid's algorithm for GCD
def gcd(a, b):
  if b > a:
    a, b = b, a
  if b == 0:
    return a
  r = a % b
  return gcd(b, r)

# LCM of two numbers a, b is a*b/gcd(a,b)

def lcm(a, b):
  return a*b/gcd(a, b)


# The problem is simply asking for the LCM of all numbers
# from 1 to 20

def main():
  result = 2
  x = 3
  while x <= 20:
    result = lcm(result, x)
    x += 1

  print result


if __name__ == '__main__':
  main()    
