
def sum_of_squares(num):
	sum = 0
	for x in xrange(1,num + 1):
		sum += x*x
	return sum

def quare_of_sums(num):
	sum = 0
	for x in xrange(1,num + 1):
		sum += x
	return sum * sum
		
a = sum_of_squares(100)
print a
b = quare_of_sums(100)
print b
diff = b - a
print diff