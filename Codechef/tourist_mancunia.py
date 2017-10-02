
from collections import defaultdict

class Graph:
  
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		for i in range(vertices):
			self.graph[i] = []
		self.adj_matrix = [[0 for i in range(n)] for j in range(n)]
		self.Time = 0
  
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)
 
	def rmvEdge(self, u, v):
		for index, key in enumerate(self.graph[u]):
			if key == v:
				self.graph[u].pop(index)
		for index, key in enumerate(self.graph[v]):
			if key == u:
				self.graph[v].pop(index)
 
	def DFSCount(self, v, visited):
		count = 1
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				count = count + self.DFSCount(i, visited)        
		return count
 
	def isValidNextEdge(self, u, v):
		if len(self.graph[u]) == 1:
			return True
		else:
			visited =[False]*(self.V)
			count1 = self.DFSCount(u, visited)
			self.rmvEdge(u, v)
			visited =[False]*(self.V)
			count2 = self.DFSCount(u, visited)
			self.addEdge(u,v)
			return False if count1 > count2 else True
 
	def printEulerUtil(self, u):
		for v in self.graph[u]:
			if self.isValidNextEdge(u, v):
				self.adj_matrix[u][v] = 1
				self.rmvEdge(u, v)
				self.printEulerUtil(v)
 
	def printEulerTour(self):
		self.graph_copy = self.graph
		u = 0
		flag = 0
		for i in range(self.V):
			if len(self.graph[i]) %2 != 0 :
				flag = 1
				break
		if flag == 1:
			print("NO")
			return False
		else:
			print("YES")
			self.printEulerUtil(u)
			return True


	def checkEdge(self, u, v):
		if self.adj_matrix[u][v] == 1:
			print(str(u+1) + " " + str(v+1))
		elif self.adj_matrix[v][u] == 1:
			print(str(v+1) + " " + str(u+1))

	


n, e = list(map(int, input().split()))
g = Graph(n)

list_of_vertex = []

for i in range(e):
	u, v = list(map(int, input().split()))
	list_of_vertex.append([u-1, v-1])
	g.addEdge(u-1, v-1)

flag = g.printEulerTour()


if flag == True:
	for i in range(len(list_of_vertex)):
		u = list_of_vertex[i][0]
		v = list_of_vertex[i][1]
		g.checkEdge(u, v)
