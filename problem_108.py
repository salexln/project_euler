
"""
http://www.cut-the-knot.org/arithmetic/ShortEquationInReciprocals.shtml
"""


"""
find all a*b*c = num
"""
# def multiplications_combanation(num):
# 	ss = set()
# 	x = 1	
# 	while(1):
# 		y = 1
# 		while(1):
# 			if x * y > num:
# 				break

# 			z = num / (x*y)			
# 			if num == z * y * x:
# 				ss.add((x,y,int(z)))

# 			y += 1

# 		if x > num:
# 			break
# 		x += 1
	
# 	return ss


# def multiplications_combanation_squere(num):
# 	"""
# 	if a,b,c > 0 : 
# 		if 1/a + 1/b = 1/c => a^2 + b^2 + c^2 is a squere
# 	"""
# 	a = 1
# 	while True:
# 		b = 1
# 		while True:
# 			if 						
# 			c = 1
# 			while True




"""
we'll search a,b > 0 such that 
x = a + n, y = b + n and n^2 = a * b
"""

import math

def find_solution(num):
	s = set()
	a = 1
	while True:

		b = 1
		while True:
			res = int(pow(num, 2))
			x = a*b
			# print a, b 
			if x == res:
				s.add((num + a, num + b))
			
			if x > res:
				break
			b += 1

		if a > num:
			break
		a += 1
	return s




# def find_solutions(num):
# 	s = set()

# 	x = num + 1
# 	while True:
# 		# print x
# 		y = 1
# 		while True:			

# 			res = ((float((x * y)) / float((x + y))))
# 			# print x, y , res

# 			if res == num:
# 				s.add((x,y,num))
# 				print 'found: ', x, y, res

# 			if res > num:
# 				break
# 			y += 1
# 			# if y == 30:
# 			# 	exit(0)

# 		if 1/x > num:
# 			break
# 		x += 1



num = 4
while True:
	s = find_solution(num)
	
	print num, len(s)
	if len(s) > 1000:
		print num
		break

	num += 1
