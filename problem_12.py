import math
from utils import euler_utils
import sympy


def triangular_num(num):
	ret  = int(num * (num + 1) / 2)
	return ret


def find_divisors(num):
	i = 1;
	div_count = 1
	
	factors = sympy.ntheory.factor_.factorint(num)		
	
	for f in factors:
		div_count *= (factors[f] + 1)

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