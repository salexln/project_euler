
sum = 0
for x in xrange(1,1000):
	if x % 5 == 0 or x % 3 == 0 and not x % 15 == 0:		
		sum += x
print sum
	