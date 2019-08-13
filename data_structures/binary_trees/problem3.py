"""
Given an integer n, construct all possible binary search trees
with n nodes where all values from [1, ..., n] are used.
"""

class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def make_trees(low, high):
	trees = []

	if low > high:
		trees.append(None)
		return trees

	for i in range(low, high + 1):
		left = make_trees(low, i - 1)
		right = make_trees(i + 1, high)

		for l in left:
			for r in right:
				node = Node(i, left=l, right=r)
				trees.append(node)

	return trees


def decode_tree(root):
	result = []

	if root:
		result.append(root.data)
		result += decode_tree(root.left)
		result += decode_tree(root.right)

	return result


def construct_trees(num):
	trees = make_trees(1, num)
	for tree in trees:
		print(decode_tree(tree))


def main():
	construct_trees(5)


if __name__ == '__main__':
	main()
