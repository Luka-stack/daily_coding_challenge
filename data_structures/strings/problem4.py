"""
You are given a string of length n and an integer k. The string can be 
manipulated by taking one of the first k letters and moving it to the end of the string.
Write a program to determine the lexicographically smallest string that can be created after
an unlimited number of moves.

For example. suppose we are given the string daily and k = 1. The best we can create
in this case is ailyd
"""

# This solustion is based on daily coding challange solution
def get_best_word(string, k):
	string = list(string)

	if k == 1:
		best = string
		for i in range(1, len(string)):
			if string[i:] + string[:i] < best:
				best = string[i:] + string[:i]
		return ''.join(best)
	
	else:
		return ''.join(sorted(string))


def main():
	test = "ccbcba"
	test_two = 'daily'

	print(get_best_word(test, 1))
	print(get_best_word(test, 5))
	print(get_best_word(test_two, 1))
	print(get_best_word(test_two, 3))


if __name__ == '__main__':
	main()