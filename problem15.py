import math
import timeit
'''
Problem 15: Grid Path Permitation

This was originally solved using DP (had to handle the risky
boundary conditions properly). Later came across a simpler 
solution using combinatorics
'''


# Combinatorics solution 
def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n-1)

def combination(n, k):
    return fac(n) / (fac(k) * fac(n-k))

# DP Method
# Every node in the boundary will have only one path from the origin
# NOT 1 + the path above it. This boundary condition is only for
# the left anf top boundary
def solveDP(m,n):
    lim = max(m,n) + 1
    C = [[0 for i in range(lim)] for j in range(lim)]
    for i in range(lim):
        for j in range(lim):
            if i == 0 or j == 0: 
                C[i][j] = 1
            else:
	        C[i][j] = C[i-1][j] + C[i][j-1]
    return C[m][n]

def main():
    start = timeit.default_timer()
    print solveDP(20,20)
    #print combination(40,20)
    print timeit.default_timer() - start
if __name__ == "__main__":
    main()
