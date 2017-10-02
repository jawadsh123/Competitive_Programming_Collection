
t = int(input())
ans = []


for i in range(t):

	n = int(input())
	c = []

	for j in range(n):
		ip = list(map(int, input().split()))
		c.append(ip)

	stopLooping = False
	removedCols = [False for j in range(n)]

	while !stopLooping:

		for j in range(n):
			diffFound = False
			for k in range(n):
				if removedCols[k]==False and diffFound==False and c[j][k]!=0:
					first = c[j][k]
				if removedCols[k]==False and diffFound==False:
