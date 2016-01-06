

def is_pentagon(num):
	x = 1
	while x < num:
		pen = x * (3 * x - 1) / 2
		if pen == num:			
			return True
		x += 1
	return False





def find():	
	ll = []
	s = set()
	for x in xrange(1,100000):	
		pen = x * (3 * x - 1) / 2
		# if is_pentagon(x):
		ll.append(pen)
		s.add(pen)
	print 'done'

	for x in ll:
	
		# print x		
		# for y in xrange(1,1000):		
		for y in ll:
			# if is_pentagon(y):				
			diff = abs(x - y)
			sum = x + y
			if diff in s and sum in s:
				print diff
				return
	# print ll

find()