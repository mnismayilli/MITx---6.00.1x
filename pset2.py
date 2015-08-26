def evaluate_poly(poly, x):
	"""
	Computes the polynomial function for a given value x. Returns that value. Example: 4 3 2
	>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
		# f(x) = 7.0x + 9.3x + 5.0x
	>>> x = -13 4 3 2 >>> print evaluate_poly(poly, x) 
		# f(-13) = 7.0(-13) + 9.3(-13) + 5.0(-13) 180339.9
	poly: tuple of numbers, length > 0
	x: number
	returns: float
	"""
	total = 0.0
	for n in range(len(poly)):
		total = poly[n] * (x ** n)
    	total = total + 1
	return total

print evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), 3)
print evaluate_poly((-13.39, 0.0, 17.5, 3.0, 1.0), 4)


def compute_deriv(poly):
	"""
	Computes and returns the derivative of a polynomial function. If the
	derivative is 0, returns (0.0,).
	Example:
	>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)  # x4 + 3.0x3 + 17.5x2 - 13.39
	>>> print compute_deriv(poly)
	(0.0, 35.0, 9.0, 4.0)
	poly: tuple of numbers, length > 0
	returns: tuple of numbers
	"""
	deriv = []
	if len(poly) < 2:
		return [0.0]
	for m in range(1,len(poly)):
		deriv.append(float(m * poly[m]))
	return deriv

print compute_deriv([1,2,3,4])
print compute_deriv([1])


