# 1 2 4 7 10 13 16 19 22 25 28 31 34 37 40

t = int(input())
ans = []

for i in range(t):
	n = int(input())

	good_set = [1, 2, 4]

	if n > 3:
		for j in range(3, n):
			val = good_set[-1] + 3
			good_set.append(val)
	else:
		good_set = good_set[0:n]

	ans.append(good_set)

for good_set in ans:
	for val in good_set:
		print(val, end=" ")
	print()
