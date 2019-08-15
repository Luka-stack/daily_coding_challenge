"""
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned to a variable-length binary string, such as 0101 or 111110,
where shorter lengths correspond to more common letters. To accomplish this,
a binary tree is built such that the path from the root to any leaf uniquely
maps to a character. When traversing the path, descending to a left child
corresponds to a 0 in the prefix, while descending right corresponds to 1.
Here is an example tree:
	    root
     0/      \1
    0/ \1   0/ \1 
   0/   a   t   \1
   c             s
With this coding, "cats" would be responted ad 0000110111

Given a dictionary of character frequencies, build a Huffman tree, and use it to
determine a mapping between character and their encoded binray strings.
"""
import heapq


class Node:
	def __init__(self, char, left=None, right=None):
		self.char = char
		self.left = left
		self.right = right


def build_tree(frequencies):
	nodes = []
	
	for char, frequency in frequencies.items():
		heapq.heappush(nodes, (frequency, Node(char)))

	while len(nodes) > 1:
		f1, n1 = heapq.heappop(nodes)
		f2, n2 = heapq.heappop(nodes)
		node = Node('#', n1, n2)
		heapq.heappush(nodes, (f1+f2, node))

	return nodes[0][1] # root


def encode(root, string='', mapping={}):
	if not root:
		return

	if not root.left and not root.right:
		mapping[root.char] = string

	encode(root.left, string + '0', mapping)
	encode(root.right, string + '1', mapping)

	return mapping


if __name__ == '__main__':
	frequencies = { 'a': 3, 'c': 6, 'e': 8, 'f': 2 }
	tree = build_tree(frequencies)
	print(encode(tree))
	