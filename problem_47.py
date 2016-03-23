from utils import euler_utils
import sympy
import math


def how_many_distinct_primes(num):
	 factors = euler_utils.get_factors(num)	
	 return len(factors())



count = 0

num = 4
while True:
	if sympy.ntheory.isprime(num):
		num += 1
		continue
	else:
		if how_many_distinct_primes(num) == 4 and how_many_distinct_primes(num + 1) == 4\
		 and how_many_distinct_primes(num + 2) == 4 and how_many_distinct_primes(num + 3) == 4:
			print num, num + 1, num + 2, num + 3
			break

	num += 1
