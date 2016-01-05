import math


s = set()
for a in xrange(2, 101):
	for b in xrange(2, 101):
		temp = int(math.pow(a,b))
		s.add(temp)


print len(s)
