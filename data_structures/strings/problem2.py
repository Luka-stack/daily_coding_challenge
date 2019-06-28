"""
Given a list of words, find all pairs of unique indices such that
the concatention of the two words is a polindrome.

For example. given the list ['code', 'edoc', 'da', 'd'], return [(0,1), (1,0), (2,3)]
"""

# Brutus
def catch_polindrome(words):
	result = []

	for idx, v_one in enumerate(words):
		for jdx, v_two in enumerate(words):
			if idx == jdx:
				continue;
			if is_polindrome(v_one + v_two):
				result.append((idx, jdx))
	return result


def is_polindrome(word):
	return word == word[::-1]


# Much more elegant way :)
def pretty_catch(words):
	result = []
	vocab = {}

	# Create vocabulary from given words
	for idx, val in enumerate(words):
		vocab[val] = idx

	for idx, val in enumerate(words):
		# take all sufixes and prefixes from word
		for size in range(len(val)):
			prefix, sufix = val[:size], val[size:]
			reversed_prefix = prefix[::-1]
			reversed_sufix = sufix[::-1]

			# ababa = ab|aba / aba<-has to be polindrome / and then you add /
			# ba to aba and get -> abababa <- palindrome
			if is_polindrome(sufix) and reversed_prefix in vocab:
				if idx != vocab[reversed_prefix]:
					result.append((idx, vocab[reversed_prefix]))

			if is_polindrome(prefix) and reversed_sufix in vocab:
				if idx != vocab[reversed_sufix]:
					result.append((idx, vocab[reversed_sufix]))

	return result

def main():
	words = ['code', 'edoc', 'da', 'd']

	print(catch_polindrome(words))
	print(pretty_catch(words))


if __name__=='__main__':
	main()
