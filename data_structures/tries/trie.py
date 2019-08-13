ENDS_HERE = "#"

class Trie:
	def __init__(self):
		self._trie = {}

	def insert(self, text):
		trie = self._trie
		for char in text:
			if char not in trie:
				trie[char] = {}
			trie = trie[char]
		trie[ENDS_HERE] = True

	def find(self, prefix):
		trie = self._trie
		for char in prefix:
			if char in trie:
				trie = trie[char]
			else:
				return None
		return trie


def insert_words(words, trie):
	for word in words:
		trie.insert(word)


def print_trie(trie):
	_helper_print(trie._trie)


def _helper_print(trie_dict, nesting = -3):
	if type(trie_dict) == dict:
		print('')
		nesting += 3
		for val in trie_dict:
			print(nesting * ' ', end='{\'')
			print(val, end='\':')
			_helper_print(trie_dict[val], nesting)
	else:
		print(trie_dict, "}" * (nesting//3))

	
if __name__ == '__main__':
	words = ['dog', 'dingo', 'zebra', 'cat']

	trie = Trie()
	insert_words(words, trie)
	print_trie(trie)