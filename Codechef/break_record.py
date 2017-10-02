

n = int(input())

s = list(map(int, input().split()))


mini = s[0]
maxi = s[0]
worst_count = 0
best_count = 0
for i in range(n):
	if s[i] < mini:
		worst_count += 1
		mini = s[i]
	if s[i] > maxi:
		best_count += 1
		maxi = s[i]

print(best_count, worst_count)
