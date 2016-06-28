# Assumes a sorted array. Assumes value is in array.

def binary_search(array, value, index=0):
	if len(array) == 1:
		return index

	midpoint = len(array)/2

	if array[midpoint] == value:
		return index + midpoint
	elif array[midpoint] > value:
		return binary_search(array[:midpoint], value, index)
	elif array[midpoint] < value:
		return binary_search(array[midpoint:], value, index+midpoint)


test = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for i in range(9):
	print 'search result: ', binary_search(test, i)
	print 'actual index:  ', test.index(i), '\n'