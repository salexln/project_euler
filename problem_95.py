from utils import euler_utils
import sympy

def sum_of_dividors(num):
	ll = euler_utils.get_dividors(num)

	div_sum = 0
	for x in ll[:-1]:		
		div_sum += x

	return div_sum
	
def find_amicable_chain(num):
	chain = []
	chain.append(num)

	found = {}
	found[num] = True
	
	while True:
		# we should not exeed 1000000
		if num > 1000000:
			return []		
		new_num = sum_of_dividors(num)		

		if new_num == chain[0]:
			return chain
		
		if found.get(new_num):
			return []

		if new_num == 0 or new_num == 1:
			return []
		
		chain.append(new_num)
		found[new_num] = True
		num = new_num

	return chain

num = 1
max_chain = []
while num < 1000000:	
	if sympy.ntheory.isprime(num):
		num += 1
		continue
	chain = find_amicable_chain(num)

	if len(chain) > len(max_chain):
		max_chain = chain

	num += 1


print 'max_chain = ',max_chain

min_member = max_chain[0]

for x in max_chain:
	if x < min_member:
		min_member = x

print 'min_member = ',min_member


