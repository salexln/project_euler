import math
from fractions import gcd
import sympy


def is_polyndrom(num):
	ll = [int(i) for i in str(num)]	
	size = len(ll) -1	
	for i in xrange(0, size):		
		if ll[i] != ll[size - i]:
			return False
	return True

def is_prime(num):
	if num == 0 or num == 1:
		return False
	if num == 2:
		return True

	temp = 2
	while temp < math.sqrt(num) + 1:
		if num % temp == 0:
			return False
		temp += 1
	return True


phi_map = {}
def factorize(num):
	primes = set()
	for x in phi_map:		
		if num % x == 0:						
			primes.add(x)			
			# num /= x		
	return primes	

def phi(num):	
	count = 1

	if is_prime(num):
		phi_val = num - 1
		phi_map[num] = phi_val
		return phi_val
	
	primes = factorize(num)		
	temp = 1.0
	for x in primes:		
		temp *= float(1-1/float(x))

	return temp*num

def is_permutation(a, b):
	ll = [int(i) for i in str(a)]	
	s = set()
	for x in ll:
		s.add(x)

	ll2 = [int(i) for i in str(b)]	
	s2 = set()
	for y in ll2:
		s2.add(y)

	if len(ll) != len(ll2):
		return False	
	if s != s2:
		return False
	return True

def factorial(num):
	if num == 0:
		return 0			
	temp = 1
	for x in xrange(1,num + 1):		
		temp *= x
	return temp

def choose(n, p):
	if n < p:
		return -1
	val = factorial(n) / (factorial(p) * factorial(n-p))
	return val

def get_digits(num):
	ll = [int(i) for i in str(num)]
	return ll

def create_num_from_list(ll):
	num = 0
	for x in ll:
		num *= 10
		num += x
	return num



def find_num_of_divisors(num):
	i = 1;
	div_count = 1
	
	factors = sympy.ntheory.factor_.factorint(num)		
	
	for f in factors:
		div_count *= (factors[f] + 1)

	return div_count	

"""
returne the factors without the powers:
i.e 12 => 2,3
"""
def get_factors(num):
	factors = sympy.ntheory.factor_.factorint(num)		
	return factors.keys
	

def get_dividors(num):
	return sympy.divisors(num)