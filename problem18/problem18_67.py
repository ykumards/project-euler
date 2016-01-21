import timeit

"""
Problem 18 and 67

First instinct was to chalk out a greedy algorithm. It obviously didn't work.

The DP solution does a bottom-up transisition. Calculates the optimal path
to reach each node (important to identify the proper state, as usual,
choosing each row as state can never be solved using DP)

Uncomment the appropriate file, to solve 18 or 67

Runtime around 0.01s for Problem 67, as the Problem Statement states,
looking at each solution will take 20 billion years!
"""

def greedy():
    f = open('data.txt','r')
    index, sum = 0, 0
    for line in f:
        line = line.strip().split(' ')
        if len(line) == 1:
            index, sum = 0, int(line[0])
            continue
        # We can only move to eh neighbors of the element in the
        # lower row, so their index has to be index or index + 1
        larger = max(line[index], line[index+1])
        print larger
        sum += int(larger)
        index = line.index(larger)

    print sum
    f.close()

def DP():
    f = open('data.txt', 'r')
    # solve problem 67
    #f = open('p067_triangle.txt','r')
    l = []
    sum = 0
    # Read the data from file and add to a 2D list
    for line in f:
        l.append(map(int,line.strip().split(' ')))
    # List comprehension here will be faster than using map

    # Creating a memoization matrix 'M'
    rows = len(l)
    cols = len(l[rows-1])
    M = [[0 for i in range(rows)] for j in range(len(l))]

    for i in xrange(len(l)):
        maxPath = 0
        for j in xrange(len(l[i])):
            pathwt = int(getPath(i,j,M,l))
            if maxPath < pathwt:
                maxPath = pathwt
        sum = maxPath
    print "Optimal path produces the sum: ", sum
    f.close()


def getPath(i,j,M,l):
    if i == 0 and j == 0:
        M[i][j] = l[i][j]
    elif j == 0:
        M[i][j] = l[i][j] + M[i-1][j]
    elif j+1 == len(l[i]):
        M[i][j] = l[i][j] + M[i-1][j-1]
    else:
        M[i][j] = l[i][j] + max(M[i-1][j], M[i-1][j-1])
    return M[i][j]

def main():
    start = timeit.default_timer()
    DP()
    print "Runtime:", timeit.default_timer() - start

# Just for reference, one of the best solutions from the discussion thread
# This raises the question, do we really need a separate matrix M?
# Depends on whether we will reuse the matirix l, code clarity, etc
def superSolution():
    l=[[int(number) for number in line.split()] for line in open("p067_triangle.txt",'r')]
    rowcount=len(l)
    for i in range(rowcount-2, -1,-1):
	       for j in range(0,i+1):
		             l[i][j]=max(l[i+1][j],l[i+1][j+1])+l[i][j]
    print l[0][0]

if __name__ == "__main__":
    main()
