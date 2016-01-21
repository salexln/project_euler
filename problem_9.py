



for i in xrange(0,1000):
	for j in xrange(i,1000):
		for k in xrange(j,1000):
			if i + j + k == 1000:
				if i*i + j*j == k*k:
					print i, j, k 
					print i*j*k