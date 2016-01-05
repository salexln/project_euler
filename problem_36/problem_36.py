
def is_polyndrom(num):
	ll = [int(i) for i in str(num)]	
	size = len(ll) -1	
	for i in xrange(0, size):		
		if ll[i] != ll[size - i]:
			return False
	return True


sum = 0
for x in xrange(1, 1000001):
	 a = "{0:b}".format(x)
	 if is_polyndrom(a) and is_polyndrom(x):
	 	sum += x

print sum