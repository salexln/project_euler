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

def truncatable_primes(num):
	ll = [int(i) for i in str(num)]

	#rempve left:
	for x in xrange(0, len(ll)):		
		
		temp = []
		for y in xrange(0, x+1):
			temp.append(ll[y])

		# create a number
		total = 0
		for i in xrange(0, len(temp)):
			total *= 10
			total += temp[i]
		if not is_prime(total):
			return False	
		
		# print 30*'*'
		temp2 = []
		for y in xrange(0, x+1):
			temp2.append(ll[len(ll) - y - 1])
			
		# create a number
		total2 = 0
		for i in xrange(0, len(temp2)):
			total2 *= 10
			total2 += temp2[len(temp2) - 1- i]
		if not is_prime(total2):
			return False
	return True

count = 0
x = 8
sum = 0
while count < 11:
	if truncatable_primes(x):
		print x	
		count += 1
		sum += x
	x += 1


print 'sum = ', sum