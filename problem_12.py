import math
from utils import euler_utils


def triangular_num(num):
	ret  = int(num * (num + 1) / 2)
	return ret


def find_divisors(num):
	div_count = euler_utils.find_num_of_divisors(num)

	if div_count > 500:
		return True
	return False


num = 1
while True:		
	tri_num = triangular_num(num)

	
	if find_divisors(tri_num):
		print tri_num
		break
	num += 1