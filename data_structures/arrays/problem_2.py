"""
Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted.
For example. given [3, 7, 5, 6, 9], you should return (1,3)
"""


def find_window(array):
	sort_array = sorted(array)
	beg, end = None, None

	for idx in range(len(array)):
		if array[idx] != sort_array[idx] and not beg:
			beg = idx
		elif array[idx] != sort_array[idx]:
			end = idx

	return (beg, end)


def smallest_window(array):
	beg, end = None, None
	max_visited, min_visited = -float('inf'), float('inf')

	for idx in range(len(array)):
		max_visited = max(max_visited, array[idx])
		if array[idx] < max_visited:
			end = idx

	for idx in range(len(array) - 1, -1, -1):
		min_visited = min(min_visited, array[idx])
		if array[idx] > min_visited:
			beg = idx

	return (beg, end)


def main():
	test_array = [3, 7, 5, 6, 9]

	print(find_window(test_array))
	print(smallest_window(test_array))


if __name__ == '__main__':
	main()
