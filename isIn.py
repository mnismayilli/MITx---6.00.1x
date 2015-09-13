def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string
	returns: True if char is in aStr; False otherwise
	'''
	if aStr == "":
		return False
	elif len(aStr) == 1:
		if char == aStr:
			return True
		return False
	else:
		mid = len(aStr)/2
		if char == aStr[mid]:
			return True
		elif char > aStr[mid]:
			return isIn(char, aStr[mid+1 : ])
		else: 
			return isIn(char, aStr[:mid])


print isIn('m', 'acdglmnqyz')  # True          
print isIn('a', 'acdglmnqyz')  # True
print isIn('z', 'acdglmnqyz')  # True
print isIn('b', 'acdglmnqyz')  # False
print isIn('a','c')  # False
print isIn('a', '')  # False