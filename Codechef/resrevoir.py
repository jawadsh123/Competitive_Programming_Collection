
t = int(input())
ans = []

for i in range(t):
	n, m = list(map(int, input().split()))
	res = []
	for j in range(n):	
		ip = input()
		res.append(ip)

	stable = True

	for j in range(n):
		for k in range(m):
			ele = res[j][k]
			if ele == "B":
				if j != n-1 and res[j+1][k] != "B":
					stable = False
					break
			elif ele == "W":
				if k == 0 or k == m-1 or j == n-1:
					stable = False
					break
				elif res[j][k-1] == "A" or res[j][k+1] == "A" or res[j+1][k] == "A":
					stable = False
					break

	if stable:
		ans.append("yes")
	else:
		ans.append("no")

for x in ans:
	print(x)

