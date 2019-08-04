"""
Given a binary tree, return the level of the tree that has the minimum sum.
The level of a node is defined as the number of connections required to get
to the root, with the root having level zero
For example:
	   1	
	  / \
	 2   3
	 	/ \
	   4   5
In this tree, level 0 has sum 1, level 1 has sum 5, and level 2 has sum 9, 
so the level with the minimum sum is 0
"""
from collections import defaultdict, deque


def min_sum_lvl(root):
	queue = deque([])
	queue.append((root, 0))

	lvl_to_sum = defaultdict(int)

	while queue:
		node, lvl = queue.popleft()
		lvl_to_sum[lvl] += node.data

		if node.right:
			queue.append((node.right, lvl+1))

		if node.left:
			queue.append((node.left, lvl+1))

	return min(lvl_to_sum, key=lvl_to_sum.get)


##### Test Code #####
class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def tree_lvl(root, lvl=0):
	result = []

	if root:
		result.append(f'lvl: {lvl} data: {root.data}')
		result += tree_lvl(root.left, lvl+1)
		result += tree_lvl(root.right, lvl+1)

	return result


def main():
	tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
	tree_two = Node(10, Node(2, Node(5), Node(-1)), Node(2, Node(9), Node(2, Node(0))))

	print('First Tree; Level:', min_sum_lvl(tree))
	print(tree_lvl(tree))
	assert min_sum_lvl(tree) == 0

	print('\nSecond Tree; Level:', min_sum_lvl(tree_two))
	print(tree_lvl(tree_two))
	assert min_sum_lvl(tree_two) == 3


if __name__ == '__main__':
	main()
