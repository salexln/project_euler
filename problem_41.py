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


def all_digits(num):
	ll = [int(i) for i in str(num)]	
	s = set()
	for x in ll:
		s.add(x)

	if len(s) != len(ll):
		return False

	for x in xrange(1, len(ll) + 1):
		if not x in s:
			return False

	return True

# print all_digits(2143)

max = 0
for x in xrange(1, 1000000000):	
	if all_digits(x):
		if is_prime(x):
			print x
			if x > max:
				max = x

print max