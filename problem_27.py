import math

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

def count_primes(a, b):
	n = 1
	count = 0
	while True:
		num = n*n + n*a +b 
		if num < 0:
			break
			
		if is_prime(num):
			count += 1
		else: 
			break
		n += 1
	return count

max = 0
max_product = 0

for a in xrange(-1000,1000):
	for b in xrange(-1000,1000):
		print a,b 
		primes = count_primes(a,b)
		if primes > max:
			max = primes
			max_product = a * b


print max_product
