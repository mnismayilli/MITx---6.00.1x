def csum(numbers):
	"""
	create a addition function
	"""
	total = 0
	for num in numbers:
		total = total + num
	return total

sum_list = [1, 3, 5, 2, 9, 7]
print csum(sum_list)



def cproduct(numbers):
	"""
	create a multiplication
	"""
	product = numbers[0]
	for num in numbers:
		product = product * num
	return product

product_list = [2, 7, 5, 3, 10]
print cproduct(product_list)



def cmax(numbers):
	"""
	create a function that only return the biggest number from list
	"""
	biggest_number = numbers[0]
	for num in numbers:
		if biggest_number <= num:
			biggest_number = num
	return biggest_number

max_list = [8, 20, 30, 5]
print cmax(max_list)



def cmin(numbers):
	"""
	create a function that only return the smallest number from list
	"""
	smallest = numbers[0]
	for num in numbers:
		if smallest >= num:
			smallest = num
	return smallest

min_list = [3, 5, 1, 7]
print cmin(min_list)