from utils import euler_utils
import math


def check_if_pandigital(ll):
	s = set()
	prev_size = 0
	for x in ll:
		if x == 0:
			return False		
		s.add(x)
		if prev_size == len(s):
			# no progress was made....
			return False
		prev_size = len(s)
	
	if len(s) == 9:
		return True
	return False

def check_9_last_pandigital(num):	
	ll = euler_utils.get_digits(num)[-9:]
	if len(ll) < 9:
		return False
	return check_if_pandigital(ll)


def check_9_first_pandigital(num):
	ll = euler_utils.get_digits(num)[:9]
	return check_if_pandigital(ll)


MOD = 1e9

last_prev = 1
last_prev_prev = 1
last_curr = 0

prev = 1
prev_prev = 1
curr = 0

found = False
count = 2

while not found:
	count += 1
	# print count
	last_curr = last_prev + last_prev_prev
	last_curr = int(last_curr % MOD)
	last_prev_prev = last_prev
	last_prev = last_curr


	curr = prev + prev_prev
	prev_prev = prev
	prev = curr

	if check_9_last_pandigital(last_curr):
		print count
		if check_9_first_pandigital(curr):
			found = True

print 'Final = ', count
# print curr












