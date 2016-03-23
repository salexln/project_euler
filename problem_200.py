from utils import euler_utils
import math
import sympy


def is_sqube(num):
	factors = euler_utils.get_factors(num)

	if len(factors()) != 2:
		return False

	a = factors()[0]
	b = factors()[1]

	if (math.pow(a,2) * math.pow(b,3) == num) or (math.pow(b,2) * math.pow(a,3) == num):
		return True

	return False

def is_prime_proof(num):
	ll = euler_utils.get_digits(num)

	for i in xrange(0, len(ll)):
		x = ll[i]
	
		for y in xrange(0,10):			
			if y == x:
				continue	

			ll[i] = y
 			new_num = euler_utils.create_num_from_list(ll)
 			if sympy.ntheory.isprime(new_num):
 				return False
 			ll[i] = x

 	return True
 				
def contains_200(num):
	if str(200) in str(num):
		return True
	return False





found = 0
num = 1
while found < 200:
	if contains_200(num):
		if is_sqube(num):
			if is_prime_proof(num):
				print num
				found += 1

	num += 1

