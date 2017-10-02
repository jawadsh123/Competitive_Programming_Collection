
t = int(input())
ans = []

for i in range(t):
	ip = list(map(int, input().split()))
	c = ip[0]
	d = ip[1]
	l = ip[2]
	total = c + d
	l2 = l//4

	if c > 2*d:
		ex = c - 2*d + d
	else:
		ex = d

	if l2 >= ex and l2 <= total and l%4 == 0:
		ans.append("yes")
	else:
		ans.append("no")

for x in ans:
	print(x)