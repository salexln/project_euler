import math

def sum_fact(num):
	ll = [int(i) for i in str(num)]	
	sum = 0
	for x in ll:
		sum += math.factorial(x)
	return sum

def find_factorial_chain(num):
	chain_size = 1
	s = set()
	s.add(num)	
	curr = num
	while True:
		curr = sum_fact(curr)
		if curr in s:
			return chain_size
		chain_size += 1
		s.add(curr)

count = 0
for x in xrange(1,1000001):	
	if find_factorial_chain(x) == 60:
		count += 1

print count