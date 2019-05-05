"""
Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the orginal array except
the one at i.

For Example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

## using division

def avoid_index(array):
	total = 1
	for i in array:
		total *= i

	return [total//i for i in array]


## without division

def brutus(array):
	result = [1] * len(array)
	for idx, val in enumerate(array):
		for jdx in range(len(result)):
			if jdx == idx:
				continue
			result[jdx] *= val

	return result 


def find_products(array):
	forward  = [1] * len(array)
	backward = [1] * len(array)

	for idx in range(1, len(array)):
		forward[idx]  = forward[idx - 1] * array[idx - 1]
		backward[-idx - 1] = backward[-idx] * array[-idx]

	return [f * b for f, b in zip(forward, backward)]

# [1, 2, 3, 4, 5]
# -> [1, 1, 1, 1, 1] -> [         1,   (1*1)=1,  (2*1)=2, (3*2)=6, (4*6)=24] 
# <- [1, 1, 1, 1, 1] -> [(2*60)=120, (3*20)=60, (4*5)=20, (5*1)=5,        1]

## Solustion From Book

def products(nums):
	# arr = [1, 2, 3, 4, 5]
	# Generate prefix products.
	prefix_products = []
	for num in nums:
		if prefix_products:
			prefix_products.append(prefix_products[-1] * num)
		else:
			prefix_products.append(num)
	# [1, 2, 3,  4,   5]
	# [1, 2, 6, 24, 120]

	# Generate suffix products.
	suffix_products = []
	for num in reversed(nums):
		if suffix_products:
			suffix_products.append(suffix_products[-1] * num)
		else:
			suffix_products.append(num)
	suffix_products = list(reversed(suffix_products))
	# [5, 4, 3, 2, 1]
	# [5, 20, 60, 120, 120]
	# rev [120, 120, 60, 20, 5]

	# Generate result from the product of prefixes and suffixes.
	result = []
	for i in range(len(nums)):
		if i == 0:
			result.append(suffix_products[i + 1])
		elif i == len(nums) - 1:
			result.append(prefix_products[i - 1])
		else:
			result.append(suffix_products[i + 1] * prefix_products[i - 1])

	return result


## Testing

def main():
	test_array1 = [3, 2, 1]
	test_array2 = [1, 2, 3, 4, 5]

	print(avoid_index(test_array1))
	print(avoid_index(test_array2))
	print(brutus(test_array1))
	print(brutus(test_array2))
	print(find_products(test_array1))
	print(find_products(test_array2))
	print(products(test_array1))
	print(products(test_array2))


if __name__ == '__main__':
	main()
