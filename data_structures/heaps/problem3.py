"""
A regular number in mathematics is defined as one which evenly divides some power
of 60. Equivalently, we can say that a regular number is one whose only prime 
divisors are 2, 3 and 5
These numbers have had many applications, from helping ancient Babylonians keep
time to tunning instruments according to the diatonic scale.
Given a integer n, write a program that generates, in order, the first n regular numbers
"""
import heapq

def calculate_regular_naive(length):
	pow_two   = [2 ** i for i in range(length)]
	pow_three = [3 ** i for i in range(length)]
	pow_five  = [5 ** i for i in range(length)]

	result = set()
	for two in pow_two:
		for three in pow_three:
			for five in pow_five:
				result.add(two * three * five)

	return sorted(result)[:length]


def calculate_regular(length):
	result = [1]
	last, count = 0,0

	while count < length:
		x = heapq.heappop(result)
		if x > last:
			yield x
			last = x
			count += 1
			heapq.heappush(result, 2 * x)
			heapq.heappush(result, 3 * x)
			heapq.heappush(result, 5 * x)


if __name__ == '__main__':
	regular_15	= list(calculate_regular(15))
	regular_0 	= list(calculate_regular(0))
	
	naive_regular_15	= calculate_regular_naive(15)
	naive_regular_0 	= calculate_regular_naive(0)

	assert regular_15 == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
	assert regular_0  == []

	assert naive_regular_15 == regular_15
	assert naive_regular_0  == regular_0
