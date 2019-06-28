"""
Given two singly linked lists that intersect at some point, find the intersecting node.
Assume the lists are non-cyclical
For example, given A = 3 - > 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with
value 8. In this example, assume node with the same value are the exact same node object.

Do this in O(m+n) time (where m and n are the length of the lists) and constant space
"""

def size(node):
	if not node:
		return 0
	return 1 + size(node.next)

def find_intersect(node_1, node_2):
	size_1, size_2 = size(node_1), size(node_2)
	curr_1, curr_2 = node_1, node_2

	if size_1 > size_2:
		for _ in range(size_1 - size_2):
			curr_1 = curr_1.next
	else:
		for _ in range(size_2 - size_1):
			curr_2 = curr_2.next

	while curr_1 != curr_2:
		curr_1 = curr_1.next
		curr_2 = curr_2.next

	return curr_1


class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def main():
	#A = 3 - > 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10
	equal = Node(8, Node(10))
	A = Node(3, Node(7, equal))
	B = Node(99, Node(1, equal))

	assert find_intersect(A, B) is equal

if __name__=='__main__':
	main()