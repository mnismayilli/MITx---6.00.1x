# 1
def int_to_string(list_number):
	"""
	print multiplication table
	"""
	new_list = []
	for num in list_number:
		element = str(num)
		new_list.append(element) 
	return new_list

for num in range(1, 11):
	multiples_of_num= range(num, num * 10 + 1, num)
	print  num, ":", ' '.join(int_to_string(multiples_of_num))


# 2
for multiplicator in range(1, 11):
	print multiplicator, " : ",
	for multiplier in range(1, 11):
		print multiplicator * multiplier,
	print ''


# 3
print '\n'.join('{}: {}'.format(n, ' '.join([str(i * n) for i in range(1, 11)])) for n in range(1, 11))
