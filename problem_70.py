from utils import euler_utils
import math




min_n = 0
min_val = 0.0

max_val = int(math.pow(10, 7))
for n in xrange(2,max_val):
	print n
	phi = int(euler_utils.phi(n))
	if euler_utils.is_permutation(n, phi):
		# print n, phi
		# print float(n)/phi
		ratio = float(n)/phi
		if min_val == 0:
			min_val = ratio
			min_n = n
		if ratio < min_val:
			min_val = ratio
			min_n = n

print min_n, min_val