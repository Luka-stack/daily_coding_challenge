"""
Given a linked list, rearrange the node values such that they appear in alternating
low -> high -> low -> high -> ... form.
For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4
"""

# keeping track of even elements
def rearrange_nodes(node):
	even = True
	cur = node

	while cur.next:
		if cur.data > cur.next.data and even:
			cur.data, cur.next.data = cur.next.data, cur.data

		elif cur.data < cur.next.data and not even:
			cur.data, cur.next.data = cur.next.data, cur.data

		even = not even
		cur = cur.next
		
	return node

# keeping current and prev node in memory
def alternate(node):
	prev = node
	cur = node.next

	while cur:
		if prev.data > cur.data:
			prev.data, cur.data = cur.data, prev.data
		if not cur.next:
			break
		if cur.next.data > cur.data:
			cur.next.data, cur.data = cur.data, cur.next.data

		prev = cur.next
		cur = cur.next.next

	return node

# Test Code
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def show_list(node):
	while node is not None:
		print(node.data, end=" -> ")
		node = node.next		
	print()


def main():
	root = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	root_2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	#root_2 = Node(2, Node(1, Node(3, Node(9, Node(2)))))

	print("Base: ")
	show_list(root)

	print("\nRearrange (first function):")
	root = rearrange_nodes(root)
	show_list(root)

	print("\nRearrange (second function):")
	root_2 = alternate(root_2)
	show_list(root_2)

if __name__=='__main__':
	main()