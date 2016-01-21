import math


def digit_sum(num):
	ll = [int(i) for i in str(num)]
	sum = 0
	for x in ll:
		sum += x
	return sum


num = int(math.pow(2,1000))

print num
print digit_sum(num)