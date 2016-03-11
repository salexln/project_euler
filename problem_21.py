



def get_sum_dividors(num):
	sum = 0
	for i in xrange(1,int(num/2) +1):
		if num % i == 0:
			sum += i

	return sum


count = 0
for x in xrange(1,10001):
	num = get_sum_dividors(x)

	if num == x:
		continue

	num2 = get_sum_dividors(num)
	if num2 == x:			
		count += x
		count += num

print count/2