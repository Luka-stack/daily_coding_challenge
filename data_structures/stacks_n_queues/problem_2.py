"""
Given a string of round, curly, and square opening and closing brackers, return whether
the brackets are balanced (well-formed).
For example, given the string '([])[]({})', you should return true.
Given the string '([)]' or '((()', you should return false.
"""

def well_formed(stru):
	stack = []

	for ch in stru:
		if ch in ['(', '{', '[']:
			stack.append(ch)
		else:
			if not stack:
				return False

			if (ch == ')' and stack[-1] != '(') or \
			   (ch == ']' and stack[-1] != '[') or \
			   (ch == '}' and stack[-1] != '{'):
			   	return False

			stack.pop()

	return len(stack) == 0


def main():
	test_str_1 = '([])[]({})'
	test_str_2 = '([)]'
	test_str_3 = '((()'

	assert well_formed(test_str_1) is True
	assert well_formed(test_str_2) is False
	assert well_formed(test_str_3) is False


if __name__ == '__main__':
	main()