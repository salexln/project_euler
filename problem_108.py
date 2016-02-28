
"""

1/x + 1/y = 1/n 

	<=>
x = n + s, y = n + r

...
	<=>
rs = n^2

"""

import math

def find_square_mult(num):
	count = 0
	s = 1
	while True:
		if s > num:
			break

		r = 1
		while True:
			if r*s > int(math.pow(num,2)):
				break

			if r*s == int(math.pow(num,2)):
				# print s + num, r + num, num
				count += 1
			r += 1
		s += 1
	return count

# print find_square_mult(1000)

num = 4  
while True:
	res = find_square_mult(num)
	print num , res
	if res > 1000:
		print num
		break

	num += 1