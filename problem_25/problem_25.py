
def num_of_digits(num):
	ll = [int(i) for i in str(num)]
	return len(ll)

prev_prev = 1
prev = 1

idx = 2
while True:
	idx += 1
	curr = prev_prev + prev
	if num_of_digits(curr) == 1000:
		print idx
		break
	prev_prev = prev
	prev = curr

