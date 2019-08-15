"""
Compute the running median of sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far after each new element.
Recall that the median of an even-numered list is the average of the two
middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
	2; 1.5; 2; 3.5; 2; 2; 2
"""
import heapq


def get_median(min_heap, max_heap):
	if len(min_heap) > len(max_heap):
		min_val = heapq.heappop(min_heap)
		heapq.heappush(min_heap, min_val)
		return min_val
	elif len(min_heap) < len(max_heap):
		max_val = -heapq.heappop(max_heap)
		heapq.heappush(max_heap, -max_val)
		return max_val
	else:
		min_val = heapq.heappop(min_heap)
		max_val = -heapq.heappop(max_heap)
		heapq.heappush(min_heap, min_val)
		heapq.heappush(max_heap, -max_val)
		return (min_val + max_val) / 2


def consume_one(num, min_heap, max_heap):
	if len(min_heap) + len(max_heap) <= 1:
		heapq.heappush(max_heap, -num)
		#heapq.heappush(min_heap, num)
		return

	median = get_median(min_heap, max_heap)
	if num > median:
		heapq.heappush(min_heap, num)
	else:
		heapq.heappush(max_heap, -num)


def rebalace_heap(min_heap, max_heap):
	if len(min_heap) > (len(max_heap) + 1):
		root = heapq.heappop(min_heap)
		heapq.heappush(max_heap, -root)
	elif len(max_heap) > (len(min_heap) + 1):
		root = -heapq.heappop(max_heap)
		heapq.heappush(min_heap, root)


def running_median(array):
	min_heap = []
	max_heap = []
	result = []
	for v in array:
		consume_one(v, min_heap, max_heap)
		rebalace_heap(min_heap, max_heap)
		result.append(get_median(min_heap, max_heap))
	return result


if __name__ == '__main__':
	
	assert running_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
	assert running_median([]) == []
	assert running_median([1]) == [1]
	assert running_median([-1, -5]) == [-3]
	