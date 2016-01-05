

def is_polyndrom(num):
	ll = [int(i) for i in str(num)]	
	size = len(ll) -1	
	for i in xrange(0, size):		
		if ll[i] != ll[size - i]:
			return False
	return True


max = 0
for i in xrange(0,1000):
	for j in xrange(0,1000):		
		temp = i * j 
		if(is_polyndrom(temp)):			
			if temp > max:	
				max = temp
	
print 'Max = ', max

