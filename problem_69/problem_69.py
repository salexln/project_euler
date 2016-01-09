import math
from fractions import gcd


# def gcd(a, b):
# 	return a if b == 0 else gcd(b, a % b)

def is_prime(num):
	if num == 0 or num == 1:
		return False
	if num == 2:
		return True

	temp = 2
	while temp < math.sqrt(num) + 1:
		if num % temp == 0:
			return False
		temp += 1
	return True

phi_map = {}

def factorize(num):
	primes = set()
	for x in phi_map:		
		if num % x == 0:						
			primes.add(x)			
			# num /= x		
	return primes	

def phi(num):	
	count = 1

	if is_prime(num):
		phi_val = num - 1
		phi_map[num] = phi_val
		return phi_val
	
	primes = factorize(num)		
	temp = 1.0
	for x in primes:		
		temp *= float(1-1/float(x))

	return temp*num

max = 0.0
max_n = 2
for x in xrange(2, 1000000):			
	# print x
	temp = float(x) / float(phi(x)) 
	# print temp
	if(temp > max):
		max = temp
		max_n = x

print max_n