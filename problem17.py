import math

"""
Problem 17

Learn to spell out all the numbers properly before attempting this!
There's scope for memoization, but the speed issue only arises when scaled
much higher
"""

def getDigit(n):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    else:
        return ""

def getTeens(n):
    if n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"

def getMid(n):
    if n >= 20 and n < 30:
        return "twenty " + getDigit(n % 20)
    elif n >= 30 and n < 40:
        return "thirty " + getDigit(n % 30)
    elif n >= 40 and n < 50:
        return "forty " + getDigit(n % 40)
    elif n >= 50 and n < 60:
        return "fifty " + getDigit(n % 50)
    elif n >= 60 and n < 70:
        return "sixty " + getDigit(n % 60)
    elif n >= 70 and n < 80:
        return "seventy " + getDigit(n % 70)
    elif n >= 80 and n < 90:
        return "eighty " + getDigit(n % 80)
    else:
        return "ninety " + getDigit(n % 90)

def getHundreds(n):
    if n == 1000: return "one thousand"
    # We only care about 3 digit numbers
    hun = "hundred"
    hundreds = int(str(n)[0])
    others = int(str(n)[1:])
    if others == 0:
        return getDigit(hundreds) + " " + hun
    else:
        return getDigit(hundreds) +" "+  hun + " and " + wordify(others)

def wordify(n):
    if n <= 10:
        return getDigit(n)
    elif n <= 19:
        return getTeens(n)
    elif n < 100:
        return getMid(n)
    else:
        return getHundreds(n)

def main():
    sum = 0
    for i in xrange(1, 1001):
        print wordify(i)
        sum += len(wordify(i).replace(' ',''))
    print sum

if __name__ == "__main__":
    main()
