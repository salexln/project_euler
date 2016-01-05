

def factorial(num):
	if num == 0:
		return 0			
	temp = 1
	for x in xrange(1,num + 1):		
		temp *= x
	return temp


def digit_sum(num):
	ll = [int(i) for i in str(num)]
	sum = 0
	for x in ll:
		sum += x
	return sum


fact = factorial(100)
print 100, digit_sum(fact)