'''
Problem 9

Find the Pythogorean triplet so that the sum of the digits
is 1000

Used a very brute forcey method to solve this.
Useful optimization is a < b < c
'''

def main():
  for a in xrange(1, 1000):
    for b in xrange(a, 1000 - a):
      c = 1000 - b - a
      if a**2 + b**2 == c**2:
        print a * b * c
        break
    else: continue
    break

if __name__ == '__main__':
  main()
