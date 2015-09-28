#1
def sharp(x):
	"""
	x is an integer, and x >= 2
	"""
	if x == 2:
		return 2
	return  (sharp(x-1))**x

print sharp(2)  # 2
print sharp(4)  # 4096
print sharp(10)  # it's gonna return a suuuuuuuuper big number!

#2
def ndigits(x):
	"""
	x is an integer, and x >= 2
	"""
	if x/10 == 0:
		return 1
	return 1 + ndigits(x/10)

print ndigits(6)  # 1
print ndigits(3456789)  # 7
print ndigits(1234567890098765432345678986546)  # 31

#3
print ndigits(sharp(7)) + 2*ndigits(sharp(6)) + ndigits(sharp(5)) + ndigits(sharp(4))  #1000
