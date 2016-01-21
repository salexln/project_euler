

def is_same_digits(a, b):
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


def find():
	x = 1
	while True:
		if is_same_digits(x, x*2):
			if is_same_digits(x, x*3):
				if is_same_digits(x, x*4):
					if is_same_digits(x, x*5):
						if is_same_digits(x, x*6):
							print x
							return
		x += 1

find()

	