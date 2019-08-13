"""
Implement a PrefixMapSum class with the following methods:
	* insert(key: str, value: int): Set a given key's value in the map.
									if the key already exists, overwrite the value
	* sum(prefix: str): Return the sum of all values of keys that begin with a given prefix
For example, you should be able to run the following code:
	mapsum.insert("columnar", 3)
	assert mapsum.sum("col") == 3
	mapsum.insert("column", 2)
	assert mapsum.sum("col") == 5
"""
from collections import defaultdict
import time

WORDS = ['transmit', 'transaction', 'translation', 'transfer', 'anticlimax', 'antiaircraft', 'antiseptic', 'antibody']
PREFIX = 'anti'

# Insertion: O(1), Sum: O(n*k) 
# <n number of words inserted, k length of the prefix>
class PrefixMapSum_insertionfocus:
	def __init__(self):
		self._map = {}

	def insert(self, key: str, value: int):
		self._map[key] = value

	def sum(self, prefix: str):
		return sum(value for key, value in self._map.items() if key.startswith(prefix))


# Insertion: O(k**2), Sum: O(1)
# # <k length of the prefix>
class PrefixMapSum_sumfocus:
	def __init__(self):
		self._map = defaultdict(int)
		self.words = set()

	def insert(self, key: str, value: int):
		if key in self.words:
			value -= self.map[key]
		self.words.add(key)

		for i in range(1, len(key)+1):
			self._map[key[:i]] += value

	def sum(self, prefix: str):
		return self._map[prefix]


# Insertion & Sum: O(k)
# <k length of the prefix>
class TrieNode:
	def __init__(self):
		self._dict = {}
		self.total = 0


class PrefixMapSum_equal:
	def __init__(self):
		self._map = {}
		self._trie = TrieNode()

	def insert(self, key: str, value: int):
		value -= self._map.get(key, 0)
		self._map[key] = value

		trie = self._trie
		for char in key:
			if char not in trie._dict:
				trie._dict[char] = TrieNode()
			trie = trie._dict[char]
			trie.total += value

	def sum(self, prefix: str):
		trie = self._trie
		for char in prefix:
			if char in trie._dict:
				trie = trie._dict[char]
			else:
				return 0
		return trie.total


def check_execution(trie):
	insertion_time = 0
	for idx, w in enumerate(WORDS):
		start_time = time.time()
		trie.insert(w, idx)
		insertion_time += time.time() - start_time

	sum_time = time.time()
	trie.sum(PREFIX)
	sum_time = time.time() - sum_time

	return {'insert': insertion_time, 'sum': sum_time}


if __name__ == '__main__':

	insert_trie = PrefixMapSum_insertionfocus()
	sum_trie    = PrefixMapSum_sumfocus()
	equal_trie  = PrefixMapSum_equal()
	
	# times are merely illustrative
	print(f'Insertion Focus Trie; Times: {check_execution(insert_trie)}')
	print(f'Sum Focus Trie; Times: {check_execution(sum_trie)}')
	print(f'Equal Trie; Times: {check_execution(equal_trie)}')

	assert insert_trie.sum(PREFIX) 	== 22
	assert sum_trie.sum(PREFIX) 	== 22
	assert equal_trie.sum(PREFIX) 	== 22
	