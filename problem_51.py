from utils import euler_utils


def replace(num, digits):
	ll = euler_utils.get_digits(num)
	# print 'll = ', ll
	smallest = 0
	# for x in digits:
	temp = ll
	count = 0
	for x in xrange(0,10):
		# for y in xrange(0,10):
		temp[digits[0]] = x
		temp[digits[1]] = x
		num = euler_utils.create_num_from_list(temp)
		if len(euler_utils.get_digits(num)) == len(ll):
			if euler_utils.is_prime(num):
				count += 1
				if smallest == 0:
					smallest = num
				if num < smallest:
					smallest = num
	if count == 7:
		return smallest
	else:
		return -1
	
			
# print replace(56003, [2,3])

num = 1
while True:
	ll = euler_utils.get_digits
	for x in xrange(1,len(ll)):
		digits = []
		while len(digits) < x:
			
			
		
