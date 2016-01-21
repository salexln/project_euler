import math

def get_triangle_num(num):
	sum = 0
	for x in xrange(1,num):
		sum += x
	return sum

def count_devidors(num):
	div = 1 #including itself
	temp = 1
	while temp < num/2 + 1:
		if num % temp == 0:
			# print temp
			div += 1
		temp += 1
	return div



# print count_devidors(28)
x = 1
max = 0
while True:
	temp = get_triangle_num(x)		
	div = count_devidors(temp)
	if div > max:
		max = div
	print max
	# print x, temp, div
	# print temp, count_devidors(temp)
	if(div > 500):
		print temp
		break
	x += 1
