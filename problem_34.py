

def factorial(num):
	if num == 0:
		return 0			
	temp = 1
	for x in xrange(1,num + 1):		
		temp *= x
	return temp

def digit_factorial(num):
	ll = [int(i) for i in str(num)]
	sum = 0
	for x in ll:
		sum += factorial(x)
	if sum == num:
		return True
	# if sum > num:
	# 	exit(0)
	return False


sum = 0
for x in xrange(3,20000000):	
	if digit_factorial(x):
		print x
		sum += x

print 'sum = ', sum

