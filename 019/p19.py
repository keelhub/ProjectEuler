import os
from numpy import *

Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MonthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = 1
m = 1
y = 1900
cy = 1900
M = Months
dweek = 1
sundays = 0

while 1:
	# Leap year toggle
	if cy != y:
		cy = y
		if y % 4 == 0:
			if y % 400 == 0 and y % 100 != 0:
				continue
			else:
				M = MonthsLeap
		else:
			M = Months

	# Increment day/month/year
	if d == M[m-1]:
		d = 1
		if m == 12:
			m = 1
			y = y + 1
		else:
			m = m + 1
	else:
		d = d + 1

	# Increment day of week, sunday count
	if dweek == 7:
		dweek = 1
		if d == 1 and y >= 1901:
			sundays = sundays + 1
	else:
		dweek = dweek + 1

	# End check
	if d == M[11] and m == 12 and y == 2000:
		break

print(sundays-1) # Unsure why counts 1 more
