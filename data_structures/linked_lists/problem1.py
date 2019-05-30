"""
Given the head of a singly linked list, reverse it in-place
"""

def reverse_bigger(node):
 	head, _ = _reverse_bigger(node)
 	return head

def _reverse_bigger(node):
 	if node is None:
 		return None, None

 	if node.next is None:
 		return node, node

 	head, tail = _reverse_bigger(node.next)
 	node.next = None
 	tail.next = node
 	return head, node

# O(n) time and constant time
def reverse(head):
	prev, current = None, head

	while current is not None:
		tmp = current.next
		current.next = prev
		prev = current
		current = tmp
	return prev


# Test Code
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def show_list(node):
	while node is not None:
		print(node.data)
		node = node.next		


def main():
	root = Node("A", Node("B", Node("C")))
	
	print('Normal:')
	show_list(root)
	print('Reversed:')
	root = reverse(root)
	show_list(root)

	print('Normal:')
	show_list(root)
	print('Reversed:')
	root = reverse_bigger(root)
	show_list(root)

if __name__=='__main__':
	main()