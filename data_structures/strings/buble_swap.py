def bubble_swap(string, i, j):
	string = list(string)

	# Rotate so that i is at the begining.
	while i > 0:
		string = string[1:] + string[:1]
		i -= 1

	# Move the first two letters to the end in reversed order.
	string = string[:1] + string[2:] + string[1:2]
	string = string[1:] + string[:1]

	# Rotate back to the initial position.
	while len(string) > j + 1:
		string = string[1:] + string[:1]
		j += 1

	return ''.join(string)