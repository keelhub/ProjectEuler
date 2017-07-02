import math
from numpy import *
#from sets import Set

def FindAllDivisors(x):
    divList = array([1])
    y = 2
    while y <= math.sqrt(x):
        if x % y == 0:
            divList=append(divList, y)
            divList=append(divList, int(x / y))
        y += 1
    return unique(divList)

abundant = array([], dtype=int)
for i in range(1,28125):
	if sum(FindAllDivisors(i)) > i:
		abundant = append(abundant, i)

length = count_nonzero(abundant)

a = 0
allsums = array([], dtype=int)
for x in abundant:
	a = a+1
	print(100*a/length, "%")
	allsums = append(allsums, x+abundant)
		
allsums = unique(allsums)

out = setdiff1d(range(1, 28125), allsums)

print(sum(out))
print(out)
