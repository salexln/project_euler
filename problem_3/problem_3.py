import math

def find_max(ll):
	max = ll[0]
	for x in ll:
		if x > max:
			max = x
	return max

def is_prime(num):
	if num == 1:
		return False
	temp = 2
	while temp < math.sqrt(num):
		if num % temp == 0:			
			return False
		temp += 1
	return True

def find_primes(num):
	primes = []	
	temp = 2
	while temp < math.sqrt(num):	
		if num % temp == 0 and is_prime(temp):
			primes.append(temp)
		temp += 1
	return primes


# primes = find_primes(13195)
primes = find_primes(600851475143)
print primes
print 'max = ', find_max(primes)

