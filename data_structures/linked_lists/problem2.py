"""
We can represent an integer in a linked list format by having each node represent a digit in the number.
The nodes are connected in reverse order, such that the number 54321 is represented by the following linked list:
	1 - > 2 -> 3 -> 4 -> 5
Given two linked lists in this format, return their sum.
For example, given:
	9 -> 9
	5 -> 2
You should return 124(99 + 25) as:
	4 -> 2 -> 1
"""

def add(first_head, second_head, carry=0):
	if not first_head and not second_head and not carry:
		return 0

	first_head_val  = first_head.data  if first_head  else 0
	second_head_val = second_head.data if second_head else 0
	total = first_head_val + second_head_val + carry

	first_head_next  = first_head.next  if first_head  else None
	second_head_next = second_head.next if second_head else None
	carry_next = 1 if total >= 10 else 0

	return Node(total % 10, add(first_head_next, second_head_next, carry_next))

# Test Code
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def show_list(node):
	while node:
		print(node.data)
		node = node.next		


def main():
	node_first = Node(9, Node(9))
	node_second = Node(5, Node(2))
	combined_node = add(node_first, node_second)

	print("First Node")
	show_list(node_first)
	print("\nSecond Node")
	show_list(node_second)
	print("\nCombined Node")
	show_list(combined_node)

if __name__=='__main__':
	main()