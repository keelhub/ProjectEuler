import os
import fileinput
from numpy import *

nums = zeros((15,15))
calc = zeros((15,15))

nums[0,0] = 75
nums[1,0:2] = array([95, 64])
nums[2,0:3] = array([17, 47, 82])
nums[3,0:4] = array([18, 35, 87, 10])
nums[4,0:5] = array([20, 4, 82, 47, 65])
nums[5,0:6] = array([19, 1, 23, 75, 3, 34])
nums[6,0:7] = array([88, 2, 77, 73, 7, 63, 67])
nums[7,0:8] = array([99, 65, 4, 28, 6, 16, 70, 92])
nums[8,0:9] = array([41, 41, 26, 56, 83, 40, 80, 70, 33])
nums[9,0:10] = array([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
nums[10,0:11] = array([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
nums[11,0:12] = array([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
nums[12,0:13] = array([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
nums[13,0:14] = array([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
nums[14,0:15] = array([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

calc[14,:] = nums[14,:]
for k in range(14,0,-1):
	for i in range(0,14):
		calc[k-1,i] = max(calc[k,i:i+2]) + nums[k-1,i]
	
print(calc[0,0])

l = 100
i = 0
nums = zeros((l,l))
for line in fileinput.input(files=('triangle.txt')):
	nums[i,0:i+1] = fromstring(line, dtype=int, sep=' ')
	i += 1

calc = nums
for k in range(l-1,0,-1):
	for i in range(0,l):
		calc[k-1,i] = max(calc[k,i:i+2]) + nums[k-1,i]
	
print(calc)
