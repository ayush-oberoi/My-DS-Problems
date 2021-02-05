class Graphs:
	def __init__(self):
		self.numberofnodes = 0
		self.adjacency = {}

	def addvertex(self,node):
		self.adjacency[node] = []
		self.numberofnodes += 1

	def addedge(self,node1,node2):
		self.adjacency[node1].append(node2)
		self.adjacency[node2].append(node1)

	def showgraph(self):
		allnodes = self.adjacency.keys()
		for node in allnodes:
			nodeconnection = self.adjacency[node]
			connections = ""
			for vertex in nodeconnection:
				connections += vertex + " "
			print(node + "--->" + connections)

graph = Graphs()
graph.addvertex('0')
graph.addvertex('1')
graph.addvertex('2')
graph.addvertex('3')
graph.addvertex('4')
graph.addvertex('5')
graph.addvertex('6')
graph.addedge('3','1')
graph.addedge('3','4')
graph.addedge('4','2')
graph.addedge('4','5')
graph.addedge('1','2')
graph.addedge('1','0')
graph.addedge('0','2')
graph.addedge('6','5')
graph.showgraph()