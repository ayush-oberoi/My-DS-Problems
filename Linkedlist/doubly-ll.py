class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self,data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			self.tail = self.head
			self.length += 1
		else:
			newNode.prev = self.tail
			self.tail.next = newNode
			self.tail = newNode
			self.length += 1

	def prepend(self,data):
		newNode = Node(data)
		newNode.next = self.head
		self.head.prev = newNode
		self.head = newNode
		self.length += 1

	def pop(self):
		current = self.tail
		current.prev.next = None
		self.tail = current.prev
		self.length -= 1

	def insert(self,index,data):
		new_node = Node(data)
		i = 0
		temp = self.head
		if index >= self.length:
			self.append(data)
			return
		if index == 0:
			self.prepend(data)
			return
		while i<self.length:
			if i == index-1:
				new_node.next = temp.next
				temp.next = new_node
				new_node.prev = temp
				self.length += 1
				break
			temp = temp.next
			i += 1

	def remove(self,index):
		current = self.head
		i = 0
		if index >= self.length:
			print("Wrong Index")
		if index == 0:
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
		if index == self.length-1:
			self.pop()
			return

		while i < self.length:
			if i == index-1:
				current.next = current.next.next
				self.length -= 1
				break
			i += 1
			current = current.next


	def printFromFront(self):
		current = self.head
		while current != None:
			print(current.data, end=' ')
			current = current.next
		print()

	def printFromLast(self):
		current = self.tail
		while current != None:
			print(current.data,end=' ')
			current = current.prev
		print()

MyLL = DoublyLinkedList()
MyLL.append(10)
MyLL.append(20)
MyLL.prepend(5)
MyLL.append(40)
MyLL.insert(2,30)
MyLL.append(50)
MyLL.printFromFront()
MyLL.remove(2)
MyLL.remove(4)
MyLL.pop()
MyLL.printFromFront()
MyLL.printFromLast()