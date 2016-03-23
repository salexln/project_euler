from utils import euler_utils
import sympy
import math

def was_goldbach_right(num, primes):
	for p in primes:
		for x in xrange(1,num):			
			temp = p + 2 * math.pow(x, 2)
			if num == temp:			
				return True
			if num < temp:
				break

	return False



primes = []


primes.append(2)

num = 3
while True:	
	if sympy.ntheory.isprime(num):
		primes.append(num)
	else:
		#it is composite and we need to check it		
		if not was_goldbach_right(num, primes):
			print num
			break
	
	num +=2
