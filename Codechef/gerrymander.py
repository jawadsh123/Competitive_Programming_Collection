from collections import deque

t = int(input())
ans = []

for i in range(t):

	o1, o2 = list(map(int, input().split()))
	d = list(map(int, input().split()))

	list_of_states = [0 for j in range(len(d))]
	win_que = deque()


	num_zer = 0
	num_one = 0

	for j in range(o2):

		win_que.append(d[j])

		if d[j] == 0:
			num_zer += 1
		else:
			num_one += 1

	if num_one > num_zer:
		list_of_states[0] = 1


	for j in range(1, len(d)):

		ele = win_que.popleft()

		if ele == 0:
			num_zer -= 1
		else:
			num_one -= 1

		if j <= len(d) - o2:
			if d[j + o2 - 1] == 0:
				num_zer += 1
			else:
				num_one += 1
			win_que.append(d[j + o2 - 1])

		else:
			if d[o2 - (len(d) - j) - 1] == 0:
				num_zer += 1
			else:
				num_one += 1
			win_que.append(d[o2 - (len(d) - j) - 1])

		if j >= o2:
			if num_one > num_zer:
				list_of_states[j] = list_of_states[j-o2] + 1
			else:
				list_of_states[j] = list_of_states[j-o2]
		else:
			if num_one > num_zer:
				list_of_states[j] = 1

	max_count = 0
	for j in range(len(d)):
		if list_of_states[j] > max_count:
			max_count = list_of_states[j]

	if max_count >= (o1+1)//2:
		ans.append(1)
	else:
		ans.append(0)

for x in ans:
	print(x)





		