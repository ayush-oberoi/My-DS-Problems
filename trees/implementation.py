class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self,data):
		newnode = node(data)
		if self.root == None:
			self.root = newnode
		else:
			current = self.root
			while(True):
				if data < current.data:
					if current.left == None:
						current.left = newnode
						return
					else:
						current = current.left
				else:
					if current.right == None:
						current.right = newnode
						return
					else:
						current = current.right

	def lookup(self,value):
		if self.root == None:
			print("Empty")
		current = self.root
		while(True):
			if current == None:
				return False
			elif current.data == value:
				return True
			elif value < current.data:
				current = current.left
			else:
				current = current.right 

	def print_tree(self,curr_node):
		if curr_node != None:
			self.print_tree(curr_node.left)
			print(str(curr_node.data))
			self.print_tree(curr_node.right)

	def printtree(self):
		if self.root != None:
			self.print_tree(self.root)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
print(bst.lookup(10))
bst.printtree()