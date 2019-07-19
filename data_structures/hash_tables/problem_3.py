"""
You have a large array, most of whose elements are zero.
Create a more space-efficient data structure, SparseArray, that implements the
following interface:
	* init(arr, size): initialize with the orginal large array and size
	* set(i, val): update index at i to be val
	* get(i): get the value at index i
"""

class SparseArray():
	def __init__(self, arr, size):
		self.size = size
		self._dict = {}

		for i, val in enumerate(arr):
			if val != 0:
				self._dict[i] = val

	def _check_bounds(self, i):
		if i < 0 or i >= self.size:
			raise IndexError('Out of bounds')

	def set(self, i, val):
		self._check_bounds(i)

		if val != 0:
			self._dict[i] = val
			return
		elif i in self_dict:
			del self_dict[i]

	def get(self, i):
		self._check_bounds(i)
		return self._dict.get(i, 0)


def main():
	test_arr = [1, 2, 0, 0, 0, 6, 7]
	sparse = SparseArray(test_arr, len(test_arr))

	assert sparse.get(0) == 1
	assert sparse.get(3) == 0

if __name__=='__main__':
	main()		
