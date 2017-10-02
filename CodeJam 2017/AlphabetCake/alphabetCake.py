

t = int(input())
currX = 0
currY = 0
currX_neg = 0
currY_neg = 0
visited = []
global_set = []
r, c = 0, 0


def floodFill(i, j, startX, startY):
	global currX, currY, currX_neg, currY_neg, r, c


	try:
		if visited[i][j] == True:
			return True
		else:
			visited[i][j] = True
		print(i, j, matrix[i][j])
		if matrix[i][j] != '?' and (i!=startX or j!=startY):
			if i < currX and i >= startX:
				currX = i - 1
			if i > currX_neg and i <= startX:
				currX_neg = i + 1
			if j < currY and j >= startY:
				currY = j - 1
			if j > currY_neg and j <= startY:
				currY_neg = j + 1
			print("set",i, j, matrix[i][j])
			return True
	except IndexError:	
		return True

	

	if i < r:
		floodFill(i+1, j, startX, startY)
	if i > 0:
		floodFill(i-1, j, startX, startY)
	if j < c:
		floodFill(i, j+1, startX, startY)
	if j > 0:
		floodFill(i, j-1, startX, startY)



for i in range(t):
	r, c = list(map(int, input().split(' ')))
	matrix = []

	global_set = [[False for j in range(c)] for k in range(r)]

	for j in range(r):
		ip = list(input())
		matrix.append(ip)

	print(matrix)

	for j in range(r):
		for k in range(c):
			if matrix[j][k] != '?' and global_set[j][k] == False:
				visited = [[False for l in range(c)] for m in range(r)]
				currX = c-1
				currY = r-1
				currX_neg = 0
				currY_neg = 0
				floodFill(j, k, j, k)
				print("{} : {}{}{}{}".format(matrix[j][k], currX, currY, currX_neg, currY_neg))
				# for x_idx in range(currX_neg, currX+1):
				# 	for y_idx in range(currY_neg, currY+1):
				# 		matrix[x_idx][y_idx] = matrix[j][k]
				# 		global_set[x_idx][y_idx] = True

