#Implementation using Arrays

class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class stack:
	def __init__(self):
		self.array = []

	def peek(self):
		try:
			print(self.array[len(self.array)-1])
		except:
			print("Stack is empty")

	def push(self,data):
		self.array.append(data)
	def pop(self):
		self.array.pop()

	def prints(self):
		if len(self.array) == 0:
			print("Stack is empty")
		else:
			for i in self.array[::-1]:
				print(i)


Mystack = stack()
#Mystack.peek()
Mystack.push(5)
Mystack.push(10)
Mystack.push(15)
Mystack.pop()
Mystack.pop()
#Mystack.peek()
Mystack.pop()
Mystack.prints()
#Mystack.pop()
#Mystack.prints()
