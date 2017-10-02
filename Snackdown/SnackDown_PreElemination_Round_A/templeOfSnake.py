
t = int(input())

ans = []

for i in range(t):
	n = int(input())

	heights = list(map(int, input().split(' ')))

	prefixHeight = [1 for j in range(len(heights))]
	suffixHeight = [1 for j in range(len(heights))]

	totalSum = sum(heights)
	maxHeight = 0

	for j in range(1, len(heights)):

		if heights[j] > prefixHeight[j-1]:
			prefixHeight[j] = prefixHeight[j-1] + 1
		else:
			prefixHeight[j] = heights[j]

	for j in range(len(heights)-2, -1, -1):

		if heights[j] > suffixHeight[j+1]:
			suffixHeight[j] = suffixHeight[j+1] + 1
		else:
			suffixHeight[j] = heights[j]

	for j in range(len(prefixHeight)):
		mini = min(prefixHeight[j], suffixHeight[j])

		if mini > maxHeight:
			maxHeight = mini

	ans.append(totalSum - maxHeight*maxHeight)

for x in ans:
	print(x)


		