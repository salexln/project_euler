from utils import euler_utils
import math

def square_digit(num):
	ll = euler_utils.get_digits(num)

	res = 0
	for x in ll:
		res += math.pow(x, 2)
	return int(res)

def square_digit_chain(num):	
	while num != 1 and num != 89:
		# print num
		num = square_digit(num)

	return num

count = 0

# for x in xrange(1,100):
for x in xrange(1,10000001):
	# print x
	res = square_digit_chain(x)

	# if res == 89:
	# 	print x, res
	# 	count += 1

	if res == 1:
		# print x, res
		count += 1


print 'result = ',10000000 - count


