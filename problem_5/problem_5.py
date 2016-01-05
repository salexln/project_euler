
def find_smallest(till, num):	
	i = 1
	while i < till:
		if num % i != 0:
			return False
		i += 1
	return True


found = False
num = 20
while not found:
	if find_smallest(20, num):
		found = True
		break
	num += 1

print num

