"""
Referece: https://en.wikipedia.org/wiki/Barycentric_coordinate_system

Suppose we have a triangle: v1, v2, v3  (vi = (xi, yi) )

Each point P inside the triangle can we written:
p = a*v1 + b*v2 + c*v3, a+b+c = 1, a,b,c >= 0

We'll find a, b, c by solving the following equation:


x1 x2 x3   a    0
y1 y2 y3 * b =  0
 1  1  1   c    1


"""


import numpy as np
import numpy.linalg as la

def check_barycentric_coordinate(v1, v2, v3):
	x1, y1 = v1
	x2, y2 = v2
	x3, y3 = v3

	T = np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]])

	sol = np.array([0, 0, 1])

	a,b,c =  np.linalg.solve(T, sol)
	
	if a > 0 and b > 0 and c > 0:				
		return True	
	return False




count  = 0
with open('data/p102_triangles.txt', 'r') as f:
	lines = f.readlines()
	
	for line in lines:
		x = (int(line.split(',')[0]),  int(line.split(',')[1]))
		y = (int(line.split(',')[2]),  int(line.split(',')[3]))
		z = (int(line.split(',')[4]),  int(line.split(',')[5]))

		if check_barycentric_coordinate(x,y,z):
			count += 1
print 'count = ', count