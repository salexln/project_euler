import math



def diophantine(x, y, d):
	if (math.pow(x, 2) - math.pow(y, 2) * d) == 1:
		return True
	return False



# print diophantine(3,2,2)


for d in xrange(1,7):
	pass