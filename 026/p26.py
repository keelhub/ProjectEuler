
def divide(n, d):
	if d==0:
		return 0
	if d<0: 
		return -divide(n, -d)
	if n<0:
		return -divide(-n, d)
	Q, R = 0, n
	while R >= d:
		Q = Q + 1
		R = R - d
	return R

def cyclelength(n):
	print(n)

for i in range(1,10):
	print(divide(1, i))

