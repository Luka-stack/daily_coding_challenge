"""
Implement an autocomplete system. That is, given a query string s and a set
of all possible query strings, return all strings in the set that have s as a prefix
For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal]
"""
EOB = "#"
WORDS = ["dog", "dear", "deal", "deck", "dark"]

# Dict base solution
def dict_base_complete(query):
	result = set()
	for word in WORDS:
		if word.startswith(query):
			result.add(word)

	return result


# Trie base solution
class Trie():
	def __init__(self):
		self._trie = {}

	def insert(self, word):
		trie = self._trie
		for char in word:
			if char not in trie:
				trie[char] = {}
			trie = trie[char]
		trie[EOB] = True

	def find(self, prefix):
		trie = self._trie
		for char in prefix:
			if char in trie:
				trie = trie[char]
			else:
				return None
		
		return self._elements(trie)

	def _elements(self, trie):
		result = []
		for char, value in trie.items():
			if char == EOB:
				subresult = ['']
			else:
				subresult = [char + sufix for sufix in self._elements(value)]
			result.extend(subresult)

		return result


def insert_words(words, trie):
	for word in words:
		trie.insert(word)


def complete_word(query, trie):
	sufixes = trie.find(query)
	return [query + sufix for sufix in sufixes]


if __name__ == '__main__':

	assert dict_base_complete('de') == {'deal', 'deck', 'dear'}

	trie_words = ['arm', 'axes', 'apple', 'box', 'car', 'trash']
	trie = Trie()
	insert_words(trie_words, trie)

	assert complete_word('a', trie) == ['arm', 'axes', 'apple']
