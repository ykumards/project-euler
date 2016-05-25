import math
import timeit

def divisorSum(n, dSum):
    if n in dSum:
        return dSum[n]
    ulimit = int(math.sqrt(n))
    sum = 1
    for i in xrange(2, ulimit):
        if n%i == 0:
            sum += i
            sum += n/i
    if ulimit ** 2 == n:
        sum += ulimit
    
    dSum[n] = sum
    return sum


def main():
    start = timeit.default_timer()
    amic = [0] * 10001
    dSum = {}
    for a in xrange(3, len(amic)):
        if amic[a] != 0:
            continue
        b = divisorSum(a, dSum)
        #print b
        if a !=b and a  == divisorSum(b, dSum):
            amic[a] = a
            amic[b] = b

    print sum(amic)
    print "Time:", timeit.default_timer() - start


if __name__ == "__main__":
    main()
