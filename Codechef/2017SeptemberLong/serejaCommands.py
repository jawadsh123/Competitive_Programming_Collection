
t = int(input())
ans = []

for i in range(t):

	n, m = list(map(int, input().split()))
	commands = []

	for j in range(m):
		t, l, r = list(map(int, input().split()))
		commands.append((t, l, r))

	actual_repetition_count = [0 for j in range(m)]
	pseudo_repetition_count = [0 for j in range(m)]

	for j in range(m-1, -1, -1):

		t, l, r = commands[j]
		l -= 1
		r -= 1

		if j < m-1:
			pseudo_repetition_count[j] += pseudo_repetition_count[j+1]
		if t == 2:
			actual_repetition_count[j] += pseudo_repetition_count[j] + 1
			inc = actual_repetition_count[j]

			pseudo_repetition_count[r] += inc
			if l > 0:
				pseudo_repetition_count[l-1] -= inc
		else:
			actual_repetition_count[j] += pseudo_repetition_count[j] + 1

	# print(actual_repetition_count, pseudo_repetition_count)

	final_list = [0 for j in range(n)]

	for j in range(m):

		t, l, r = commands[j]
		l -= 1
		r -= 1
		if t == 1:
			inc = actual_repetition_count[j]
			final_list[l] += inc
			if r < n-1:
				final_list[r+1] -= inc

	for j in range(1, n):
		final_list[j] += final_list[j-1]

	for j in range(0, n):
		final_list[j] = final_list[j] % 1000000007
	
	ans.append(final_list)

for x in ans:
	for idx, ele in enumerate(x):
		if idx < len(x) - 1:
			print(str(ele)+" ", end="")
		else:
			print(str(ele)+"\n", end="")

