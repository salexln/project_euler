import math

n = 1001
rounds = (n + 1)/ 2

curr = 1
x = 2
sum = 1 # starts from 1
while x <= rounds:	
	add = 2 * (x -1) # we should add this in each round
	for y in xrange(0, 4):
		curr += add
		sum += curr
	x += 1

print sum