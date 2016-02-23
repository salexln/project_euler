# coding=utf-8

"""
Instead calculation a^b ,we'll calculate log(a^b)

log(a^b) = b · log(a)
"""

import math

with open('data/p099_base_exp.txt', 'r') as f:
	
	count = 0
	max_val = 0
	max_idx = 0
	for line in f:
		count += 1
		a = int(line.split(',')[0])
		b = int(line.split(',')[1])

		res = b * math.log(a)
		if res > max_val:
			max_val = res
			max_idx = count
		# print res
	print 'count = ', max_val
	print 'index = ', max_idx
		