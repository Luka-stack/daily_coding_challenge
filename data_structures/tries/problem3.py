"""
Given an array of integers, find the maximum XOR of any two elements.
"""

class Trie:
	def __init__(self, bits):
		self._trie = {}
		self.size = bits

	# O(k) <k the logest bit sequence>
	def insert(self, item):
		trie = self._trie

		for i in range(self.size, -1, -1):
			bit = bool(item & (1 << i))
			if bit not in trie:
				trie[bit] = {}
			trie = trie[bit]

	# O(k) <k the logest bit sequence>
	def find_max_xor(self, item):
		trie = self._trie
		xor = 0

		for i in range(self.size, -1, -1):
			bit = bool(item & (1 << i))
			if (1 - bit) in trie:
				xor |= (1 << i)
				trie = trie[1 - bit]
			else:
				trie = trie[bit]

		return xor

# O(n*k) time and space
# <k the logest bit sequence, n every element>
def find_max_xor(array):
	bits = max(array).bit_length()

	trie = Trie(bits)
	for i in array:
		trie.insert(i)

	print_trie(trie)

	result = 0
	for i in array:
		result = max(result, trie.find_max_xor(i))

	return result


def print_trie(trie):
	_helper_print(trie._trie)


def _helper_print(trie_dict, nesting = -3):
	if type(trie_dict) == dict:
		print('')
		nesting += 3
		for val in trie_dict:
			print(nesting * ' ', end='\'')
			print(int(val), end='\'')
			_helper_print(trie_dict[val], nesting)


if __name__ == '__main__':

	array_test = [0, 2, 5, 7, 10]
	
	assert find_max_xor(array_test) == 15