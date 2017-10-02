

n, c = list(map(int, input().split()))

b = []
m = []

for i in range(c):
	bi, mi = list(map(int, input().split()))
	b.append(bi)
	m.append(mi)

mb = zip(m, b)

mb = list(mb)

mb.sort()

rem_box = n
no_of_match = 0

for i in range(len(mb) - 1, -1, -1):
	m, b = mb[i]
	if b <= n:
		no_of_match += m * b
		n -= b
	else:
		no_of_match += m * (n)
		n = 0
	# print(no_of_match, n, b)
	if n == 0:
		break

print(no_of_match)
