"""
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.
"""

###### O(n) Algorithm (down -> up) ######
def count_unival_subtrees(root):
	count, _ = helper(root)
	return count


def helper(root):
	if root is None:
		return 0, True

	left_count, is_left_uni = helper(root.left)
	right_count, is_right_uni = helper(root.right)
	total_count = left_count + right_count

	if is_left_uni and is_right_uni:
		if root.left is not None and root.data != root.left.data:
			return total_count, False
		if root.right is not None and root.data != root.right.data:
			return total_count, False
		return total_count + 1, True

	return total_count, False


###### O(n^2) Algorithm ######
def is_unival(root):
	return unival_helper(root, root.data)


def unival_helper(root, value):
	if root is None:
		return True

	if root.data == value:
		return unival_helper(root.left, value) and unival_helper(root.right, value)

	return False


def count_unival(root):
	if root is None:
		return 0

	left = count_unival(root.left)
	right = count_unival(root.right)

	return 1 + left + right if is_unival(root) else left + right


###### Test Code ######
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def decode_tree(root):
	result = []

	if root:
		result.append(root.data)
		result += decode_tree(root.left)
		result += decode_tree(root.right)

	return result


def main():
	tree = Node(1, Node(1), Node(1, Node(2, Node(1))))

	print('Tree:', decode_tree(tree))

	assert count_unival_subtrees(tree) == 2
	assert count_unival(tree) == 2


if __name__ == '__main__':
	main()