import sys

def isPalin(s):
  result = True
  for i in range(len(s)/2):
    if s[i] != s[-(i + 1)]:
      result = False
      break
  return result


def main():
  curr_large = 0
  for i in xrange(900, 1000):
    for j in xrange(900, 1000):
      prod = i * j
      # Turns out list comprehension is more succint, but I 
      # leave the traditional up method anyway
      if str(prod) == str(prod)[::-1] and prod > curr_large:
        curr_large = prod
  print curr_large


if __name__ == '__main__':
  main()
