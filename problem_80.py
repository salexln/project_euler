import math
from utils import euler_utils
import decimal


total_sum = 0
for y in xrange(1,101):
	
	a,b = divmod(math.sqrt(y),1)
	# print a,b
	if b == 0.0:
		continue
	
	d2 = decimal.Decimal(y)
	dot100 = decimal.Context(prec=100)

	num = str(d2.sqrt(dot100))
	# print num
	# print str(num)

	start_count = False	
	for x in str(num):
		if x == '.':
			start_count = True
			continue
		if start_count == True:
			total_sum += int(x)	

print total_sum