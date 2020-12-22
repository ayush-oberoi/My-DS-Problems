class node:
	def __init__(self,value,next=None):
		self.value = value
		self.next = next
node1 = node("3")
node2 = node("7")
node3 = node("10")
node4 = node("14")

node1.next = node2
node2.next = node3
node3.next = node4

#node1 -> node2 -> node3

currentNode = node1
while(True):
	print (f"{currentNode.value}->",end='')
	if currentNode.next is None:
		print("None")
		break
	currentNode = currentNode.next