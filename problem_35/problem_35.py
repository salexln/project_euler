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


def is_circular_prime(num):
	ll = [int(i) for i in str(num)]
	for x in ll:		
		temp = ll[0]
	
		# rotate
		for i in xrange(0, len(ll) - 1):
			ll[i] = ll[i + 1]
		ll[len(ll) - 1] = temp
		
		# create a number
		total = 0
		for i in xrange(0, len(ll)):
			total *= 10
			total += ll[len(ll) - 1 - i]
		
		if not is_prime(total):
			return False
	return True


count = 0
for x in xrange(1, 1000001):
	if is_circular_prime(x):
		count += 1	

print count
