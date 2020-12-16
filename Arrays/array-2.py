class Myarray:
	def __init__(self):
		self.length=0
		self.data={}
	def __str__(self):
		return str(self.__dict__)
	def get(self,index):
		return self.data[index]
	def push(self,item):
		self.data[self.length] = item
		self.length += 1

arr = Myarray()
arr.push(10)
arr.push('Hello')
arr.push(20)
arr.push(30)
arr.push('Ayush')
arr.push('Welcome')

