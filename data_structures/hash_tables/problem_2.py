"""
A wall consists of several rows of bricks of various integer lengths and unifrom height.
Your goal is to find a vertical line going from the top to the bottom of the wall that
cuts through the fewest number of bricks. If the line goes through the edge between
two bricks, this does not count as a cut.
"""

from collections import defaultdict

def fewest_cuts(wall):
	cuts = defaultdict(int)

	for row in wall:
		length = 0

		for brick in row[:-1]:
			length += brick
			cuts[length] += 1

	return len(wall) - max(cuts.values())


def main():

	wall_array = [[3,5,1,1], [2,3,3,2], [5,5], [4,4,2], [1,3,3,3], [1,1,6,1,1]]
	wall_array_two = [[5,5,4,4], [2,3,3,4,3,3], [1,1,2,4,2,4,4], [1,1,2,3,2,3,2,2,1,2],
					  [1,1,2,3,11], [9,2,2,2,1,2], [18]]

	assert fewest_cuts(wall_array_two) == 3
	assert fewest_cuts(wall_array) == 2


if __name__=='__main__':
	main()