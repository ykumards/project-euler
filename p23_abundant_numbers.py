import sys
import math
import timeit

# Return sum of divisors
def sum_of_divisors(n):
    result = 0
    for i in xrange(1, int(math.ceil(n/2))+1):
        if n % i == 0:
            result += i
    return result


def main():
    abundants = {}
    # Compiling a list of abundant numbers
    for i in xrange(12, 28124):
        sums = sum_of_divisors(i)
        if sums > i:
            abundants[i] = sums
    
    result_sum = 0
    # Determine if a number is sum of two abundant elements
    for ele in xrange(1, 28124):
        for first in abundants:
            if (ele-first) in abundants:
                #This means its sum of abundant numbers, hence break
                break
        else:
            result_sum += ele

    print "Sum:%d" %result_sum


if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    print "Runtime:%fs" % (timeit.default_timer() - start)
    
