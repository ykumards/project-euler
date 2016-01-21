import math
import timeit

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def main():
    start = timeit.default_timer()
    soln = fact(100)
    sum = 0
    for ch in str(soln):
        sum += int(ch)
    print "Answer:", sum
    print "Runtime:", timeit.default_timer() - start

if __name__ == "__main__":
    main()
