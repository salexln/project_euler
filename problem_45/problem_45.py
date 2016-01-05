

def triangle(num):
	return int((num * (num + 1)) / 2)

def pentagonal(num):
	return int((num * (3 * num -1)) / 2)

def hexangonal(num):
	return int(num * (2 * num - 1))


for x in xrange(50000, -1, -1):
	for y in xrange(50000, -1, -1):
		if hexangonal(x) == triangle(y):			
			# print 'found hex = pen ', x, y
			for z in xrange(50000, -1, -1):
				if triangle(z) == pentagonal(y):
					print z, y, x
					print triangle(z)