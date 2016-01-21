

def is_polyndrom(num):
	ll = [int(i) for i in str(num)]	
	size = len(ll) -1	
	for i in xrange(0, size):		
		if ll[i] != ll[size - i]:
			return False
	return True