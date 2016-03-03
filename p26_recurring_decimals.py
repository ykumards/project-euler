import timeit
"""
Find the number d (between 1-999) such that 1/d
has the longest recurring term
Example 1/7 = 0.(142857) which is 6 digits long
"""
def main():
    d_limit = 1000
    max_rep = 0
    max_rep_pos = 0
    for i in range(2, d_limit):
        rem_dict = {}
        dividend = 1
        divisor = i
        remainder = 1
        pos = 0
        rep_length = 0
        while remainder:
            remainder = dividend % divisor
            pos += 1
            if remainder not in rem_dict:
                rem_dict[remainder] = pos
            else:
                rep_length = pos - rem_dict[remainder]
                break
            if remainder < divisor:
                dividend = remainder * 10
            else:
                dividend = remainder
        if rep_length > max_rep:
            max_rep,max_rep_pos = rep_length, divisor

    print "Maximum %d repetitions for d = %d" %(max_rep, max_rep_pos)
               

if __name__ == "__main__":
    start = timeit.default_timer()
    main()
    print "Runtime: %f seconds" %(timeit.default_timer() - start)

