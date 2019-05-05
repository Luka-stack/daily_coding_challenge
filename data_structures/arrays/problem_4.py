"""
Given an array of integers, return a new array where each element in the new array is the number
of smaller elements to the right of that element in the orginal input array.
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since

	- There is 1 smaller element to the right of 3
	- There is 1 smaller element to the right of 4
	- There are 2 amaller elements to the right of 9
	- There is 1 smaller element to the right of 6
	- There are no smaller elements to the right of 1
"""

import bisect

# Brute Force
def brutus(array):
	result = []

	for idx, val in enumerate(array):
		#count = sum(x for x in array[idx:] in x < val)
		count = sum(x < val for x in array[idx:])
		result.append(count)

	return result


# Better Option
def count_less(array):
	result = []
	visited = []

	for val in reversed(array):
		position = bisect.bisect_left(visited, val)
		result.append(position)
		bisect.insort(visited, val)

	return list(reversed(result))


def main():
	array  = [3, 4, 9, 6, 1]
	array2 = [1, 2, 3, 4, 5]
	array3 = [5, 4, 3, 2, 1]
	array4 = [5, 4, 3, 4, 5]

	print('Brut')
	print(brutus(array))
	print(brutus(array2))
	print(brutus(array3))
	print(brutus(array4))
	print('Rational')
	print(count_less(array))
	print(count_less(array2))
	print(count_less(array3))
	print(count_less(array4))

if __name__ == '__main__':
	main()
