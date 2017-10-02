
t = int(input())
ans = []

for i in range(t):

	n, m = list(map(int, input().split()))
	s = input()

	posx, posy = 0, 0

	# hasMoved = False

	maxx, minx, maxy, miny = 0, 0, 0, 0

	for j in range(len(s)):

		action = s[j]

		if action == "L":
			posx -= 1
		elif action == "R":
			posx += 1
		elif action == "U":
			posy += 1
		elif action == "D":
			posy -= 1

		if posx < minx:
			minx = posx
		if posx > maxx:
			maxx = posx
		if posy < miny:
			miny = posy
		if posy > maxy:
			maxy = posy

	xRange = maxx - minx + 1
	yRange = maxy - miny + 1

	# print(xRange, yRange)

	if xRange <= m and yRange <= n:
		ans.append("safe")
	else:
		ans.append("unsafe")

for x in ans:
	print(x)