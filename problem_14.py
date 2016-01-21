


def collatz_sequence(num):
	lenght = 1
	while num != 1:		
		lenght += 1
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3 * num + 1
	return lenght


# print collatz_sequence(13)


max_chain = 0
max_num = 1

for x in xrange(1,1000000):
	chain = collatz_sequence(x)
	if chain > max_chain:
		max_chain = chain
		max_num = x

print max_num, max_chain
