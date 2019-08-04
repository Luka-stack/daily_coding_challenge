"""
Given pre-order and in-order traversals of a binary tree, wrtie
a function to reconstruct the tree.

For example, given the following pre-order traversal:
	[a,b,d,e,c,f,g]
And the following in-order traversal:
	[d,b,e,a,f,c,g]
You should return the following tree:
			a
		  /   \
		 b     c
		/ \   / \ 	
	   d   e f	 g
"""


def construct_tree(preorder, inorder):
	if not preorder and not inorder:
		return None

	if len(preorder) == len(inorder) == 1:
		return preorder[0]

	# assuming that elements of the lists are tree nodes
	# root - the first element of pre-order list
	root = preorder[0]
	root_id = inorder.index(root)

	# left subtree - all elements left to root element in in-order list
	root.left = construct_tree(preorder[1:1 + root_id], inorder[0:root_id])

	# right subtree - all elements right to root element in in-order list
	root.right = construct_tree(preorder[1 + root_id:], inorder[root_id + 1:])

	return root


##### Test Code #####
class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.right = right
		self.left = left


def preorder_tree(root):
	result = []

	if root:
		result.append(root.data)
		result += preorder_tree(root.left)
		result += preorder_tree(root.right)

	return result


def inorder_tree(root):
	result = []

	if root:
		result += inorder_tree(root.left)
		result.append(root.data)
		result += inorder_tree(root.right)

	return result


def main():
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')

	preorder = [a, b, d, e, c, f, g]
	inorder  = [d, b, e, a, f, c, g]

	tree = construct_tree(preorder, inorder)
	
	# printing preorder
	assert preorder_tree(tree) == ['a', 'b', 'd', 'e', 'c', 'f', 'g']

	# printing inorder
	assert inorder_tree(tree) == ['d', 'b', 'e', 'a', 'f', 'c', 'g']


if __name__ == '__main__':
	main()