

MAX = 4000000
prev = 2
prev_prev = 1
curr = 0

sum = 0

while curr < MAX:	
	curr = prev + prev_prev	
	if curr % 2 == 0:
		sum += curr

	prev_prev = prev
	prev = curr

# need to add the second element as well
print sum + 2
