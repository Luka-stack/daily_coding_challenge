class BinaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def _swapUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self, value):
		self.heapList.append(value)
		self.currentSize += 1
		self._swapUp(self.currentSize)

	def _swapDown(self, i):
		while (i * 2) <= self.currentSize:
			minChild = self._minChild(i)
			if self.heapList[i] > self.heapList[minChild]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[minChild]
				self.heapList[minChild] = tmp
			i = minChild

	def _minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def deleteMin(self):
		delVel = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self._swapDown(1)

		return delVel

	def heapify(self, array):
		i = len(array) // 2
		self.currentSize = len(array)
		self.heapList = [0] + array
		while i > 0:
			self._swapDown(i)
			i -= 1

if __name__ == '__main__':
	heap = BinaryHeap()

	array_to_heap = [20, 3, 2, 30, 29, 56, 3, 2]
	heap.heapify(array_to_heap)

	print(f'Array: {array_to_heap}')
	print(f'Heap: {heap.heapList[1:]}')

	heap.insert(100)
	print(f'Insert 100; Heap: {heap.heapList[1:]}')
	heap.insert(1)
	print(f'Insert 1; Heap: {heap.heapList[1:]}')

	print(f'DeleteMin {heap.deleteMin()}')
	print(heap.heapList[1:])