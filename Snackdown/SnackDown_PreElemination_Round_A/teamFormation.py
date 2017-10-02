
t = int(input())
ans = []

for i in range(t):
	n, m = list(map(int, input().split(' ')))

	for j in range(m):
		u, v = list(map(int, input().split(' ')))

	diff = n - 2*m

	if diff%2 == 0:
		ans.append("yes")
	else:
		ans.append("no")

for x in ans:
	print(x)