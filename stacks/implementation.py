#Implementation using Linked list

class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		try:
			print(self.top.data)
		except:
			print("Stack is empty")

	def push(self,data):
		mynode = node(data)
		if self.length == 0:
			self.top = mynode
			self.bottom = mynode
		else:
			holding = self.top
			self.top = mynode
			self.top.next = holding
		self.length += 1
	def pop(self):
		try:
			if self.length == 1:
				self.bottom = None
			holding = self.top
			self.top = self.top.next
			self.length -= 1
		except:
			print("Stack is empty")

	def prints(self):
		if self.length == 0:
			print("Stack is empty")
		else:
			current = self.top
			while(current != None):
				print(current.data)
				current = current.next


Mystack = stack()
Mystack.push(5)
Mystack.push(10)
Mystack.push(15)
Mystack.pop()
Mystack.prints()
Mystack.pop()
Mystack.prints()
