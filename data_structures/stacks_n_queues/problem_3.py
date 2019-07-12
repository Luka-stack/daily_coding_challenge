"""
Given an array of integers and a number k, where 1 <= k <= array length, compute
the maximum values of each subarray of length k.
For example, let's say the array is [10, 5, 2, 7, 8, 7] and k = 3. We should get
[10, 7, 8, 8], since:
	* 10 = max(10, 5, 2)
	*  7 = max(5, 2, 7)
	*  8 = max(2, 7, 8)
	*  8 = max(7, 8, 7) 
"""

from collections import deque 

def maximum_subarray(arr, k):
	q = deque()

	for i in range(k):
		while q and arr[i] >= arr[q[-1]]:
			q.pop()
		q.append(i)

	for i in range(k, len(arr)):
		print(arr[q[0]])

		while q and q[0] <= i - k:
			q.popleft()

		while q and arr[i] >= arr[q[-1]]:
			q.pop()

		q.append(i)

	return(arr[q[0]])


def minimum_subarray(arr, k):
	q = deque()

	for i in range(k):
		while q and arr[i] <= arr[q[-1]]:
			q.pop()
		q.append(i)

	for i in range(k, len(arr)):
		print(arr[q[0]])

		while q and q[0] <= i - k:
			q.popleft()

		while q and arr[i] <= arr[q[-1]]:
			q.pop()

		q.append(i)

	return(arr[q[0]])

def main():

	test_string = [10, 5, 2, 7, 8, 7]

	print('Maximum Subarray: ')
	print(maximum_subarray(test_string, 3))
	
	print('Minimum Subarray: ')
	print(minimum_subarray(test_string, 3))


if __name__ == '__main__':
	main()
