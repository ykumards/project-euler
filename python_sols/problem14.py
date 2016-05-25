import math
import timeit

# Recursive calculation gives insight on DP/Memoization
# DP improves the runtime from 30s to 2s!
def recGetChainLen(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return 1 + recGetChainLen(num/2)
    else:
        return 1 + recGetChainLen((3*num) + 1) 

def memGetChainLen(num, mem):
    if num in mem:
        return mem[num]
    else:
        if num == 1:
            return 1
        call_value = 0
        if num % 2 == 0:
            call_value = num/2
        else:
            call_value = (3 * num) + 1
        result = 1 + memGetChainLen(call_value, mem)
        mem[num] = result
        return result

########################################################
# Naive Version
def getChainLen(num):
    chain_len = 0
    while True:
        chain_len += 1
        if num == 1:
            break
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
    return chain_len

#####################################################
# Three ways to find if the number is power of two
# BitWise version is faster by 4 seconds, but is not mine

# Bitwise!
# All powers of 2 will have only one bit set to '1'
# everything else will be 0's. So remove 1 from num using (num - 1)
# will remove this 1, making the the expression equal to 0
# We also check for num != 0 to remove triviality
def isPowerTwo(number):
    return (number & (number-1) == 0) and (number != 0)

def isPowerTwo1(num):
    log2 = math.log(num, 2)
    if log2/int(log2) == 1:
        return True
    else:
        return False

def isPowerTwo2(num):
    result = True
    while num != 1 and num > 0:
        if num%2:
            result = False
        num = num/2
    return result and (num > 0)
######################################################
def main():
    start_time = timeit.default_timer()
    num_limit = 1000000
    max = (0,0)
    memo = {}
    for i in xrange(14, num_limit):
        # Powers of two will always be divided
        # doing this saves about 20s time (almost half)
        if isPowerTwo(i):
            continue
        chain_length = memGetChainLen(i, memo)
        if max[0] < chain_length:
            max = (chain_length, i)
    print "Largest chain belongs to ", max[1], "and it has chain length:", max[0]
    print "Runtime:", timeit.default_timer() - start_time

if __name__ == "__main__":
    main()         
