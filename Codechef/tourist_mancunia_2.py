
from collections import defaultdict, deque

class Graph:
  
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		for i in range(vertices):
			self.graph[i] = []
		self.Time = 0
  
	def addEdge(self,u,v,i):
		self.graph[u].append([v, i])
		self.graph[v].append([u, i])
 
	def rmvEdge(self, u, v):
		for index, key in enumerate(self.graph[u]):
			if key[0] == v:
				self.graph[u].pop(index)
		for index, key in enumerate(self.graph[v]):
			if key[0] == u:
				self.graph[v].pop(index)


	def print_euler_ckt(self):
		curr_vertex = 0

		stack = deque()

		while len(self.graph[curr_vertex]) != 0 or len(stack) != 0:
			if len(self.graph[curr_vertex]) != 0:
				next_vertex = self.graph[curr_vertex][0][0]
				list_of_vertex[self.graph[curr_vertex][0][1]] = [curr_vertex+1, next_vertex+1]

				self.rmvEdge(curr_vertex, next_vertex)
				stack.append(curr_vertex)
				

				curr_vertex = next_vertex
			else:
				curr_vertex = stack.pop()

 
	
	def euler_ckt(self):

		flag = 0

		for j in range(self.V):
			if len(self.graph[j]) % 2 != 0:
				flag = 1
				break
		if flag == 1:
			print("NO")
			return False
		else:
			print("YES")
			self.print_euler_ckt()
			return True


	

n, e = list(map(int, input().split()))
g = Graph(n)

list_of_vertex = []

for i in range(e):
	u, v = list(map(int, input().split()))
	list_of_vertex.append([u-1, v-1])
	g.addEdge(u-1, v-1, i)

flag = g.euler_ckt()

if flag == True:
	for i in range(e):
		print(str(list_of_vertex[i][0]) + " " + str(list_of_vertex[i][1]))