"""
Given a binary search tree, find the floor and ceiling of a given integer.
The floor is the highest element in the tree less than or equal to
an integer, while the ceiling is the lowest element in the tree
greater than or equal to an integer.
If either value does not exist, return None
""" 

def solution(root, x, floor=None, ceil=None):
	if not root:
		return floor, ceil

	if x == root.data:
		return (x, x)
	elif x < root.data:
		floor, ceil = solution(root.left, x, floor=floor, ceil=root.data)
	elif x > root.data:
		floor, ceil = solution(root.right, x, floor=root.data, ceil=ceil)

	return floor, ceil