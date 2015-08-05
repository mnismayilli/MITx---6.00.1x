def square_root(x):
	g = 42.0
	while g * g - x < -0.001 or g * g - x > 0.001:
		g = (g + x / g) / 2
	return g

def test():
	print square_root(9)
	print square_root(100)
	print square_root(0)
	print square_root(25)

test()
