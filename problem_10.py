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

sum = 0
for x in xrange(1,2000000):
	if is_prime(x):
		sum += x
print sum