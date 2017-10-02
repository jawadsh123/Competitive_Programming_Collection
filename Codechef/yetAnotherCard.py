
t = int(input())

ans = []

for i in range(t):

	r, b, p_r = list(map(int, input().split()))
	tot = r + b
	p_b = tot - p_r

	value = (r * p_r/tot) + (b * p_b/tot)

	ans.append(value)

for x in ans:
	print(x)