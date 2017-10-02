
t = int(input())
ans = []


for i in range(t):
	n = int(input())
	p = list(map(int, input().split()))
	p_index = dict()
	for j in range(n):
		p_index[p[j]] = j


	adj_matrix = [set() for _ in range(n)]

	for j in range(n-1):
		u, v = list(map(int, input().split()))
		u -= 1
		v -= 1
		adj_matrix[u].add(p[v])
		adj_matrix[v].add(p[u])

	for j in range(n):
		adj_matrix[j].add(p[j])

	temp_ans = ''

	p.sort()
	for j in range(n):
		flag = 0
		idx = -1
		for k in range(n-1, -1, -1):
			if p[k] not in adj_matrix[j]:
				flag = 1
				idx = p_index[p[k]]
				break
		if flag == 0:
			temp_ans += "0 "
		else:
			temp_ans += str(idx+1) + " "

	ans.append(temp_ans)	

for x in ans:
	print(x)
