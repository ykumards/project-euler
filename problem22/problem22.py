import sys
import timeit

"""
Given a text file containing several first names, 
print the score which is the sum of each names'
(position of each name * sum of the alphabetical position of each letter)
"""
def main():
    # Import the file
    f = open("names.txt")
    line = f.read()
    line = line.strip()
    names = line.split('","')
    # This will leave the first and last element
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]

    # Sorting the list by alphabets
    # sorted_names = sorted(names)

    # using list.sort() vs sorted(list)
    # list.sort() does it in place
    names.sort()
    
    # Populate the alphabet dictionary
    alphas = {}
    position = 1
    for i in xrange(65, 91):
        alphas[chr(i)] = position
        position += 1

    # Hold a global sum
    score = 0
    
    # Loop through the names list to compute the sum
    for pos in xrange(1, len(names)+1):
        worth = 0
        for ch in names[pos-1]:
            worth += alphas[ch]
        score += worth * pos

    print "Total score is: ", score

if __name__ == "__main__":
    main()
    
