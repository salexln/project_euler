# coding=utf-8

"""
calulate (28433 × 2^7830457 + 1) mod C

Phase 1:
	(A * B) mod C = (A mod C * B mod C) mod C

	(28433 × 2^7830457 mod C = ((28433 mod C) * (2^7830457 mod C) ) mod C

Phase 2:
	(A + B) mod C = (A mod C + B mod C) mod C

	(28433 × 2^7830457 + 1) mod C  = ((28433 × 2^7830457 mod C) + (1 mod C ) ) mod C

	=> Phase1 + (1 mod C ) ) mod C

"""


MOD = 1e10

def phase1():
	"""
	calc: ((28433 × 2^7830457 mod 1e10) + (1 mod 1e10 ) ) mod 1e10	
	"""	

	# calc: 2^7830457
	a = 2
	exp = 7830457

	res = 1
	while exp > 0:
		if exp % 2 == 1:
			res = (res * a) % MOD
		exp = exp >> 1
		a = (a*a) % MOD

	res2 = (28433 * res) % MOD
	return res2

def phase2(num):
	ret = num + (1 % MOD ) % MOD
	return ret


print 'running'
a = phase1()
print a
b = phase2(a)

print b