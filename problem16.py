import timeit
import math

start = timeit.default_timer()
value = int(math.pow(2,1000))
l = str(value)
sum = 0
for ch in l:
    sum += int(ch)
print sum

print "Time:", timeit.default_timer() - start
