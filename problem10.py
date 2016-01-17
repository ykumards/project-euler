import math

def isPrime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in xrange(3,int(math.ceil(math.sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True
'''
def sievePrime(limit):
    numbers = [i for i in xrange(2,limit)]
    primes = [2, 3, 5, 7, 11]
    for i in numbers:
        for p in primes:
            if 
''' 

def main():
    sum = 0
    limit = 2000000
    for i in xrange(2, limit):
        if isPrime(i):
            sum += i
    print sum


if __name__ == "__main__":
    main()
