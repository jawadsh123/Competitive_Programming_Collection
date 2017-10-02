


n, l, r = list(map(int, input().split()))

strands = list(map(int, input().split()))

strands.sort()

range_list = []


def insert_into_list(left, right):

	range_list.append([left, right]) 





for i in range(n-1, 0, -1):
	
	a = strands[i-1]
	b = strands[i]

	left_range = b - a + 1
	right_range = a + b - 1

	if left_range < l:
		if right_range < l:
			continue
		left_range = l
	if right_range > r:
		if left_range > r:
			continue
		right_range = r

	insert_into_list(left_range, right_range)


range_list.sort()

sanitized_list = []

for i in range(len(range_list)):

	curr = range_list[i]
	curr_l = curr[0]
	curr_r = curr[1]


	if len(sanitized_list) == 0:
		sanitized_list.append(curr)
		continue

	last = sanitized_list[-1]
	last_l = last[0]
	last_r = last[1]

	if curr_l <= last_r:
		if curr_r > last_r:
			sanitized_list[-1][1] = curr_r
	else:
		sanitized_list.append(curr)


count = 0

for i in range(len(sanitized_list)):

	san_curr = sanitized_list[i]

	count += san_curr[1] - san_curr[0] + 1


# print(strands, range_list, sanitized_list, count)

print(count)











