"""
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom
right until reaching the kth line, then back up to top right and so on.

For example, given the sentence "thisiszzigzag" and k = 4, you should print:
t     a     g
 h   s z   a
  i i   i z
   s     g

"""

def count_space(desc, row, height):
	if desc:
		return ((height - 1) * 2 - 1) - row * 2
	else:
		return ((height - 1) * 2 - 1) - (height - row - 1) * 2


def is_desc(idx, height):
	return idx % (2 * (height - 1)) < height - 1


def do_zigzagu(word, height):

	for row in range(height):
		#line = ["" for _ in len(word)]
		line = [""] * len(word)

		idx = row
		while idx < len(word):
			line[idx] = word[idx]
			desc = is_desc(idx, height)
			spaces = count_space(desc, row, height)
			idx += spaces + 1

		print(line)


def main():
	word = 'thisiszigzag'
	word2 = 'thisizanotherzigzag'

	do_zigzagu(word, 4)
	print('\n')
	do_zigzagu(word, 5)
	print('\n')
	do_zigzagu(word2, 5)


if __name__=='__main__':
	main()
