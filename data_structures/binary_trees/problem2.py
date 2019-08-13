"""
Given a sorted array, convert it into a height-balanced binary search tree
"""


def solution(arr):
	if not arr:
		return None

	mid = len(arr) // 2

	root = Node(arr[mid])
	root.left = solution(arr[:mid])
	root.right = solution(arr[mid + 1:])

	return root