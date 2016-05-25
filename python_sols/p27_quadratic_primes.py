import math
import timeit

def quad(a,b):
    return lambda x: x*x + a*x + b

def isPrime(x):
    #prime has to be positive
    if x < 0:
        return False
    result = True
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        result =  False
    else:
        limit = math.ceil(math.sqrt(x))
        for i in xrange(3,int(limit)+1):
            if x % i == 0:
                result = False
                break
    return result

def main():
    """
    Observations: Prime has to be positive
    So all b values must be positive (for n = 0)
    Also all b values must be prime (for n = 0)
    Now for n = 1 to hold, a > -1-b (or else
    1 + a + b wont be > 0)

    NOTE: Simple brute-force took 5s.
    Implementing these observations brough it down to 0.786s!
    """
    max_prime_count = 0
    prod = 0
    for b in xrange(2,1000):
        if not isPrime(b):
            continue
        for a in xrange(-b,1000):
            prime_count = 0
            n = 0
            #expr = quad(a,b)
            while isPrime(n*n + a*n + b):
                prime_count += 1
                n += 1
            if prime_count > max_prime_count:
                max_prime_count = prime_count
                prod = a * b

    print "Answer is: %d" %prod

if __name__ == "__main__":
    start = timeit.default_timer()
    main() 
    print "Runtime: %f seconds" %(timeit.default_timer() - start)
