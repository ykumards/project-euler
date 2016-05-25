import math

def evalPoly(n):
  sum_of_squares = (n * (n + 1) * (2*n + 1)) / 6
  square_of_sums = (n * (n + 1) * 0.5) ** 2
  result = square_of_sums - sum_of_squares
  return result


def main():

  print evalPoly(100)


if __name__ == '__main__':
  main()
