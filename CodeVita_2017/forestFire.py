
ip_1 = list(input().split(' '))
m = int(ip_1[0])
n = int(ip_1[1])

ip_2 = list(input().split(' '))
x = int(ip_2[0])-1
y = int(ip_2[1])-1

forest = []
visited = []

for i in range(m):
	forest.append(list(input().split(' ')))
	visited.append([False for j in range(n)])

isFinished = False

recentBurns = [(x, y)]
nextBurns = []

burnLevel = 1

visited[x][y] = True

while not isFinished:

	burnLevel += 1

	for burn in recentBurns:
		xburn = burn[0]
		yburn = burn[1]

		if xburn-1 >= 0 :
			if forest[xburn-1][yburn]=="T" and visited[xburn-1][yburn]==False:
				visited[xburn-1][yburn] = True
				nextBurns.append((xburn-1, yburn))

			if yburn-1 >= 0 and forest[xburn-1][yburn-1]=="T" and visited[xburn-1][yburn-1]==False:
				visited[xburn-1][yburn-1] = True
				nextBurns.append((xburn-1, yburn-1))
			if yburn+1 < n and forest[xburn-1][yburn+1]=="T" and visited[xburn-1][yburn+1]==False:
				visited[xburn-1][yburn+1] = True
				nextBurns.append((xburn-1, yburn+1))

		if xburn+1 < m :
			if forest[xburn+1][yburn]=="T" and visited[xburn+1][yburn]==False:
				visited[xburn+1][yburn] = True
				nextBurns.append((xburn+1, yburn))
			# print(xburn, yburn)

			if yburn-1 >= 0 and forest[xburn+1][yburn-1]=="T" and visited[xburn+1][yburn-1]==False:
				visited[xburn+1][yburn-1] = True
				nextBurns.append((xburn+1, yburn-1))
			if yburn+1 < n and forest[xburn+1][yburn+1]=="T" and visited[xburn+1][yburn+1]==False:
				visited[xburn+1][yburn+1] = True
				nextBurns.append((xburn+1, yburn+1))

		if yburn-1 >= 0 and forest[xburn][yburn-1]=="T" and visited[xburn][yburn-1]==False:
			visited[xburn][yburn-1] = True
			nextBurns.append((xburn, yburn-1))
		if yburn+1 < n and forest[xburn][yburn+1]=="T" and visited[xburn][yburn+1]==False:
			visited[xburn][yburn+1] = True
			nextBurns.append((xburn, yburn+1))
	# print(nextBurns)

	if len(nextBurns) == 0:
		isFinished = True
	else:
		recentBurns = nextBurns
		# print(recentBurns)
		nextBurns = []

print(burnLevel-1)




