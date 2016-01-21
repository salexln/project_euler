import math

def create_num_from_last_digits(num):
	ll = [int(i) for i in str(num)]	
	if len(ll) <= 11:
		return num

	# print ll
	# ll = ll[::-1]
	# print num
	new_num = 0
	# print ll
	# print num
	for x in xrange(len(ll) - 11, len(ll)):		
		# print x
		# print ll[x]
		new_num *= 10
		new_num += ll[x]
	# print new_num
	return new_num

# print create_num_from_last_digits(4294967296)

num = 2 * 28433
for x in xrange(1, 7830457 + 1):
	# print num
	temp = int(math.pow(num, 2))	
	num = create_num_from_last_digits(temp)


print num + 1
# print 28433 * num + 1