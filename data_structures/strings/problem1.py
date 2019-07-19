"""
Given a word 'w' and a string 's', find all indices in s which are the starting locations
of anagrams of w. For example, given w is ab and s is abxaba, return [0, 3, 4]
"""
from collections import Counter
from collections import defaultdict

# Brute Force
def is_anagram(word_one, word_two):
	return Counter(word_one) == Counter(word_two)


def find_indices(word, pattern):
	result = []

	for idx in range(len(word) - len(pattern) + 1):
		check = word[idx:idx + len(pattern)]
		if is_anagram(pattern, check):
			result.append(idx)

	return result


# good way 
def delete_from_dict(dicto, char):
	if dicto[char] == 0:
		del dicto[char]

def find_anagrams(word, pattern):
	result = []
	freq = defaultdict(int)

	for char in pattern:
		freq[char] += 1

	for char in word[:len(pattern)]:
		freq[char] -= 1
		delete_from_dict(freq, char)

	if not freq:
		result.append(0)

	for i in range(len(pattern), len(word)):
		start_char, end_char = word[i - len(pattern)], word[i]
		freq[start_char] += 1
		delete_from_dict(freq, start_char)

		freq[end_char] -= 1
		delete_from_dict(freq, end_char)

		if not freq:
			index = i - len(pattern) + 1
			result.append(index)

	return result			


def main():

	word = 'abxaba'
	pattern = 'oo'

	print(find_indices(word, pattern))
	print(find_anagrams(word, pattern))


if __name__ == '__main__':
	main()	
