#1 stupid solution
def gcdIter1(a, b):
	'''
	a, b: positive integers  
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	divisorsa = []
	for m in range(1, a+1):
		if a%m == 0:
			divisorsa = divisorsa+[m]

	divisorsb = []
	for n in range(1, b+1):
		if b%n == 0:
			divisorsb = divisorsb+[n]

	# divisorsa = []
	# divisorsb = []
	# for m in range(1, a+1):
	# 	for n in range(1, b+1):
	# 		if a%m == 0:
	# 			divisorsa = divisorsa+[m]
	# 		if b%n == 0:
	# 			divisorsb = divisorsb+[n]

	gcd = []
	for i in range(len(divisorsa)):
		for j in range(len(divisorsb)):
			if divisorsa[i] == divisorsb[j]:
				gcd.append(divisorsa[i])
	return max(gcd)

print "the greatest common divisor is:", gcdIter1(36, 27)


#2 better solution
def gcdIter2(a, b):
	'''
	a, b: positive integers  
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	c = min(a,b)
	while a % c != 0 or b % c != 0:
		c = c-1
	return c

print gcdIter2(252, 105)


#3 Euclidean algorithm
def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    c = min(a, b)
    d = max(a, b)
    if c == 0:
    	return d
    return gcdRecur(c, d-c)
print gcdRecur(252, 105)
print gcdRecur(0, 3)

def gcd(a,b):
	while b:
		a, b = b, a % b
	return a
print gcd(12,18) #6

