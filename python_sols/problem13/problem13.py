# Python makes this extremely simple


f = open('data.txt','r')
sum = 0
for line in f:
    sum += int(line)

print str(sum)[:10]
f.close()


