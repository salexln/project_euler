from utils import euler_utils


count  = 0
for n in xrange(1,100 + 1):
	for p in xrange(1,n):
		if euler_utils.choose(n, p) > 1000000:
			count += 1

print count