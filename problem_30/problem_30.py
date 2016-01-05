import math

total_sum = 0
for x in xrange(1, 10000000):
	ll = [int(i) for i in str(x)]
	sum = 0

	for y in ll:
		sum += int(math.pow(y, 5))
	if sum == x:
		print x
		total_sum += x

print 'total_sum = ', total_sum


