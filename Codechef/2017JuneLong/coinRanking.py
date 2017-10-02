
t = int(input())
ans = []

for i in range(t):
	u,v = list(map(int, input().split()))

	level = u + v + 1
	prev_level = level - 1

	rank_uptil_prev = (prev_level*(prev_level+1))//2
	rank = rank_uptil_prev + u + 1
	ans.append(rank)
	# print(level, prev_level, rank_uptil_prev, rank)

for rank in ans:
	print(rank)