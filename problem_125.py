from utils import euler_utils
import math

def is_squere_sum(num):
	
	for x in xrange(1, num):
		sq_sum = 0
		y = x
		while True:
			sq_sum += int(math.pow(y, 2))
		if sq_sum == num:
			return True

		if sq_sum > num:
			return False

	return False


MAX = int(math.pow(10, 3))
count = 0

for x in xrange(2,MAX):
	if euler_utils.is_polyndrom(x) and is_squere_sum(x):
		count += 1


print count
		
