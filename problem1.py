import math
"""
Besides the trivial solution involving a for-loop running 1000 times,
this one uses an A.P. summation. 
"""
def summation(k, size):
    # Sum of AP is simply, (n/2)(a1+an) :: an = last element
    n = math.floor((size-1)/float(k))
    # an = (a1 + (n-1) d)
    an = (k + (n-1) * k)
    
    return (n/2) * (k + an)


def main():
    print int(summation(3,1000) + summation(5,1000) - summation(15,1000))

if __name__ == "__main__":
    main()


