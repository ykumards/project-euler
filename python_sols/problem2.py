import sys
'''
Print the sum of even Fib numbers between 1 and 4 million
'''

def main():
  fibArr = []
  fibArr.append(1)
  fibArr.append(2)
  max = sum = 2
  i = 1
  while max <= 4000000:
    fibArr.append(fibArr[i] + fibArr[i-1])
    max = fibArr[i+1]
    i += 1
    if max % 2 == 0: 
      sum += max

  print sum

if __name__ == '__main__':
  main()
