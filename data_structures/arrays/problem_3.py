"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
since we would take elements 42, 14, -5 and 86. 
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would choose not 
to take any elements.

What if the elements can wrap around? For example, given [8, -1, 3, 4], return 15, as
we choose the numbers 3, 4 and 8 where the 8 is obtained from wrapping around.
"""

## Brute Force without wraping
def brutus(array):
	cur_max = 0
	n = len(array)

	for idx in range(n):
		for jdx in range(idx, n+1):
			cur_max = max(cur_max, sum(array[idx:jdx]))

	return cur_max

## without wraping
def max_subarry(array):
	cur_maximum = 0
	last = 0

	for val in array:
		last = max(val, last + val)
		cur_maximum = max(cur_maximum, last)

	return cur_maximum


def  min_subarry(array):
	cur_minimum = 0
	last = 0

	for val in array:
		last = min(val, last + val)
		cur_minimum = min(cur_minimum, last)

	return cur_minimum


def wrapping_max(array):
	max_wraparound = sum(array) - min_subarry(array)

	return max(max_wraparound, max_subarry)


def main():
	
	array =  [ 8,  -1,  3,  4]
	array2 = [34, -50, 42, 14, -5, 86]
	array3 = [-3,  -2,  3,  4,  5,  6]
	array4 = [-1,  -2, -3]

	print(brutus(array))
	print(brutus(array2))
	print(brutus(array3))
	print(brutus(array4))
	print(find_largest(array))
	print(find_largest(array2))
	print(find_largest(array3))
	print(find_largest(array4))
	print(wrapping_max(array))
	print(wrapping_max(array2))
	print(wrapping_max(array3))
	print(wrapping_max(array4))


if __name__ == '__main__':
	main()
	