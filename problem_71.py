import math
import fractions
import sympy 



def phi_list(num):
	ll = []
	if sympy.isprime(num):
		ll = list(xrange(1, num))
		return ll

	factors = sympy.ntheory.factor_.factorint(num)	

	for y in xrange(1, num):
		
		found = False
		for x in factors:
			if y % x == 0:
				found = True
				break

		if not found:
			ll.append(y)

	return ll


d = 1
val = 0
while d < 100000:
	print d
	p_ll = phi_list(d)
	
	for n in p_ll:
		num = float(n) / float(d)		
		if num > val and num < float(3) / float(7):
			val = num

	
	d += 1

print val
