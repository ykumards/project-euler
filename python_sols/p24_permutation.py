import sys
import timeit

"""
Uses the lexicographical ordering for printing the next sequence.

Say i/p is 32541, next sequence is 34125

We first loop from the end to find the element that is less than its
predecessor (here, 2 < 5). Everything after this is the tail ('541'), which will be in decreasing order.

Next we have to find the second largest element in the tail, and swap it with 2 ( so we pick 4).
After the swap, we have to sort the tail and we're done.
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
"""
def next_permutation(arr):
    # Find a non-increasing suffix, we call it 'i-1'
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    # If the sequence is already in decreasing order, we
    # have printed all permutations
    if i <= 0:
        return False
    
    # Find the second largest in the tail. Call it 'j'
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    
    # Reverse suffix
    arr[i:] = arr[len(arr)-1:i-1:-1]
    return True

"""
Prints the permutations of a given sequence.
However, we get no control on the order which is printed
"""
def permute(num_list, l, r):
    if l == r:
        global count
        count += 1
        print count, num_list
        if count == 1000000:
            print num_list
            sys.exit(0)
    else:
        for i in xrange(l, r+1):
            num_list[l],num_list[i] = num_list[i], num_list[l]
            permute(num_list, l+1, r)
            num_list[l], num_list[i] = num_list[i], num_list[l]


############ Main ###########
start = timeit.default_timer()
input_list = range(10)
n = len(input_list)
#a = list(input_str)
count = 1
while next_permutation(input_list):
    count += 1
    #print input_list
    if count == 1000000:
       print "1 Millionth permutation is", "".join([str(el) for el in input_list])
       break

print "Runtime:%fs " % (timeit.default_timer()-start)
