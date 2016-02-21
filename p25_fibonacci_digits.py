import timeit

"""
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

start = timeit.default_timer()
digi_limit = 1000
first = 1
second = 1
index = 2
digi = 1

while True:
    fib = first + second
    index += 1
    digi = len(str(fib))
    second = first
    first = fib
    if digi == digi_limit:
        print "Index: %d" %(index)
        break

print "Runtime: %fs" %(timeit.default_timer() - start)
