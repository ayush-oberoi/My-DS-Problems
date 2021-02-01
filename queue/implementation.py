class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		print(self.first.data)

	def enqueue(self,value):
		mynode = node(value)
		if self.length == 0:
			self.first = mynode
			self.last = mynode
		else:
			self.last.next = mynode
			self.last = mynode
		self.length += 1

	def dequeue(self):
		if (self.first == None):
			return None
		if self.first == self.last:
			self.last = None
		self.first = self.first.next
		self.length -= 1

	def printqueue(self):
		current = self.first
		while(current != None):
			print(current.data)
			current = current.next

myqueue = Queue()
myqueue.enqueue('Joy')
myqueue.enqueue('Matt')
myqueue.enqueue('Pavel')
myqueue.enqueue('Samir')
myqueue.dequeue()
myqueue.printqueue()

	