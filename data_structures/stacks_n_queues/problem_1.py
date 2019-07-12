"""
Implement a stack that has the follwoing metgods:
* push(val): push val onto the stack
* pop: pop off and return the topmost element of the stack. If there are no elements
	   in the stack, throw an error
* max: return the maximum value in the stack currently. If there are no elements
       in the stack, throw error	   
"""

class Stack:
	def __init__(self):
		self.stack = []
		self.maxes = []

	def push(self, val):
		self.stack.append(val)
		if self.maxes:
			self.maxes.append(max(val, self.maxes[-1]))
		else:
			self.maxes.append(val)

	def pop(self):
		if self.stack:
			self.maxes.pop()
			return self.stack.pop()
		else:
			raise IndexError("Stack is empty")

	def max(self):
		if self.maxes:
			return self.maxes[-1]
		else:
			raise IndexError("Stack is empty")


def main():
	stack = Stack()
	stack.push(5)
	stack.push(10)
	stack.push(1)

	assert stack.pop() == 1
	assert stack.max() == 10
	

if __name__ == '__main__':
	main()