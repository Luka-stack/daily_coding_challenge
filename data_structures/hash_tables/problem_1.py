"""
Implement an LRU (Least Recently Used) cache. The cache should be able to be
initialized with cache size n, and provide the following methods.
* set(key, value): set key to value. If there are already n items in the cache
	and we are adding a new item, also remove the least recently used item
* get(key): get the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""

class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None


class LinkedList:
	def __init__(self):
		# Create dummy nodes and set up head <-> tail
		self.head = Node(None, 'head')
		self.tail = Node(None, 'tail')

		self.head.next = self.tail
		self.tail.prev = self.head

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def add(self, node):
		prev = self.tail.prev
		prev.next = node
		node.prev = prev
		node.next = self.tail
		self.tail.prev = node

	def remove(self, node):
		prev = node.prev
		next = node.next
		prev.next = next
		next.prev = prev


class LRUCache:
	def __init__(self, n):
		self.size = n
		self.dict = {}
		self.list = LinkedList()

	def set(self, key, val):
		if key in self.dict:
			self.dict[key].delete()

		node = Node(key, val)
		self.list.add(node)
		self.dict[key] = node

		if len(self.dict) > self.size:
			head = self.list.get_head()
			self.list.remove(head)
			del self.dict[head.key]

	def get(self, key):
		if key in self.dict:
			node = self.dict[key]

			self.list.remove(node)
			self.list.add(node)
			return node.val


def main():
	cache = LRUCache(5)
	cache.set("1", 1)			
	cache.set("2", 2)
	cache.set("3", 3)
	cache.set("4", 4)
	cache.set("5", 5)

	assert cache.get("1") == 1
	assert cache.get("2") == 2
	assert cache.get("3") == 3
	assert cache.get("4") == 4
	assert cache.get("5") == 5
	assert cache.get("10") is None


if __name__ == '__main__':
	main()