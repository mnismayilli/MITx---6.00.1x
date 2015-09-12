# create a built-in function for computing the length of a string
def lenIter(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''
    s = 0
    for l in aStr:
    	s += 1
    return s

print lenIter("rtyu tyudfghjk")


#write a recursive function computes the length of an input argument (a string)
#by counting up the number of characters in the string.
def lenRecur(aStr):
	if aStr == '':
		return 0
	return 1 + lenRecur(aStr[1:])

print lenRecur('fghjkli678 5o')