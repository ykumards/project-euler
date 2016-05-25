import math

"""
Problem 12: Triangle number

Requires fast calculation for factors!
"""

def getTri(n):
    return int(n * (n+1) * 0.5)


# This brute - force takes up more than 1 min (rule violation for
# project euler
def getDivisorCount(num):
    count = 0
    for i in xrange(2, num/2+1):
        if num % i == 0:
            count += 1
    return count + 2

# A faster way to find the factor
# We only need to interate till the sqrt of the number
# if a is a divisor of num, then num/a will also be a divisor!! 
def get_factors(n):
    factor_count = 0
    for i in xrange(1, int(math.sqrt(n))+1):
        if n % i == 0:
            a = i
            b = n/i
            if a == b:
                factor_count += 1
            else:
                factor_count += 2
    return factor_count

# A really fast solution from StackOverflow
def factors(n):    
    return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def main():
    max_divisor = 500
    divisor_count = 0
    triangle_index = 0
    while divisor_count < max_divisor:
        triangle_index += 1
        triangle_number = getTri(triangle_index)
        divisor_count = get_factors(triangle_number)

    print "Divisor Count is", divisor_count, "for number:", triangle_number


if __name__ == "__main__":
    main()                 
