# problem 6

def count7(N):
	"""
	N: a non-negative integer
	"""
	if N == 0:
		return 0
	if N % 10 == 7:
		return 1 + count7(N/10)
	return count7(N/10)

print count7(7172377)  # 4
print count7(162538)  # 0
print count7(172)  # 1
print count7(723456098)  # 1



# problem 7

def count(x, ls):
	c = 0
	for n in range(len(ls)):
		if x == ls[n]:
			c += 1
	return c

def unique(ls):
	new_list = []
	for m in range(len(ls)):   
		if count(ls[m],ls) == 1:
			new_list.append(ls[m])
	return new_list

def uniqueValues(aDict):
	"""
	aDict: a dictionary. 
	This function takes in a dictionary and returns a list.
	"""
	values = aDict.values()
	new_values = unique(values)
	keys = aDict.keys()
	L = []
	for i in keys:
		if count(aDict[i],new_values) == 1:
			L.append(i)
			L.sort
	return L

print uniqueValues({5: 2, 0: 9, 1: 1, 2: 7, 3: 3, 6: 5, 7: 8, 9: 10, 10: 0})  # [0, 1, 2, 3, 5, 6, 7, 9, 10]
print uniqueValues({})  # []
print uniqueValues({1: 1, 2: 2, 3: 3})  # [1, 2, 3]
print uniqueValues({1: 1, 2: 1, 3: 1})  # []
print uniqueValues({0:2, 1:3, 7:2, 2:0, 3:6, 9:3})  # [2, 3]



# problem 8

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for i in reversed(range(len(L))):
    	if f(L[i]) == False:
    		L.pop(i)
    return len(L)

L = ['a', 'b', 'a', 'c', 'd']
print satisfiesF(L)  # 2
print L  # ['a', 'a']