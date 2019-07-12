"""
Simply stack implementaion based on list
"""

class Stack:
	def __init__(self):
		self.stack = []

	# add an item to stack
	def push(self, x):
		self.stack.appen(x)

	# remove the top item from stack
	def pop(sefl):
		self.stack.pop()

	# return the top item in stack
	def peek(self):
		return self.stack[-1]