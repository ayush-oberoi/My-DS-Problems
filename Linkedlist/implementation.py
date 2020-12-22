class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = None

class LinkedList:
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
			self.tail.next = newNode
			self.tail = newNode
			self.length += 1

	def prepend(self,data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode
		self.length += 1

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
				temp.next , new_node.next = new_node, temp.next
				self.length += 1
				break
			temp = temp.next
			i += 1

	def printLL(self):
		current = self.head
		while current != None:
			print(current.data, end=' ')
			current = current.next

MyLL = LinkedList()
MyLL.append(10)
MyLL.append(20)
MyLL.append(30)
MyLL.insert(2,40)
MyLL.printLL()