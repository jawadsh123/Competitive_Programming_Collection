

n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
ans = []


# creating the prefix and suffix array
prefix = [0 for i in range(n)]
suffix = [0 for i in range(n)]
for i in range(n):
	if i == 0:
		prefix[0] = 0
	elif a[i] == a[i-1]:
		prefix[i] = prefix[i-1]
	else:
		prefix[i] = i

for i in range(n-1, -1, -1):
	if i == n-1:
		suffix[i] = i
	elif a[i] == a[i+1]:
		suffix[i] = suffix[i+1]
	else:
		suffix[i] = i



for i in range(m):
	L, R, k = list(map(int, input().split()))

	L -= 1
	R -= 1

	# mid = (R - L + 1)//2 + 1
	mid = (R + L) // 2

	left = prefix[mid]
	right = suffix[mid]
	
	if prefix[mid] < L:
		left = L
	if suffix[mid] > R:
		right = R

	diff = right - left + 1

	if diff >= k:
		ans.append(a[mid])
	else:
		ans.append(-1)

for x in ans:
	print(x)

