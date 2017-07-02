#import os
#import fileinput
#from numpy import *

def divisorssum(n):
	a, b = 1, []
	while a < n:
		if n % a == 0:
			b.append(a)		
		a = a+1
	return sum(b)

print(divisorssum(100000))
ans = []
for i in range(10000):
	a = divisorssum(i)
	b = divisorssum(a)
	if b == i and a != i:
		ans.append(i)
print(sum(ans))
