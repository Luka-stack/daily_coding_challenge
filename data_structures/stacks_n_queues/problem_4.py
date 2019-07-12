"""
The  sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an
array representing whether each number is larger or smaller than the last.
Given this infromation, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]
"""

def decipher(array):
	answer, stack = [], []
	length = len(array) - 1 # from 0

	for i in range(length):
		if array[i+1] == '-':
			stack.append(i)
		else:
			answer.append(i)

			while stack:
				answer.append(stack.pop())

	stack.append(length)

	while stack:
		answer.append(stack.pop())

	return answer


def check_arr(code, arr):
	for i in range(1, len(code)):
		if code[i] == '+' and arr[i] < arr[i-1]:
			return False
		elif code[i] == '-' and arr[i] > arr[i-1]:
			return False

	return True


def main():
	cipher_1 = [None, '+', '+', '-', '+']
	cipher_2 = [None, '+', '-', '-', '-']

	resp = decipher(cipher_1)
	assert check_arr(cipher_1, resp) is True

	resp = decipher(cipher_2)
	assert check_arr(cipher_2, resp) is True

if __name__=='__main__':
	main()