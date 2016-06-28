test = [5, 2, 1, 0, 4, 3, 6]

def merge_sort(array):
	if len(array) == 1:
		return array

	midpoint = len(array)/2
	left  = merge_sort(array[:midpoint])
	right = merge_sort(array[midpoint:])

	output = []

	while len(left) > 0 and len(right) > 0:
		if left[0] < right[0]:
			output.append(left.pop(0))  # list.pop(0) removes the first item
		else:
			output.append(right.pop(0))

	if len(left) > 0:
		output.extend(left)

	if len(right) > 0:
		output.extend(right)

	return output

merge_sort(test)