
t = int(input())

ans = []

for i in range(t):

	line = input()
	ate_or_eaten = [False for _ in range(len(line))]

	snake_count = 0
	mongoose_count = 0
	eaten_count = 0

	if line[0] == "s":
		snake_count += 1
	if line[0] == "m":
		mongoose_count += 1

	for j in range(1, len(line)):

		prev = line[j-1]
		curr = line[j]

		if curr == "s":
			snake_count += 1
		if curr == "m":
			mongoose_count += 1
			
		if (not ate_or_eaten[j]) and (not ate_or_eaten[j-1]):

			if prev != curr:
				ate_or_eaten[j-1] = True
				ate_or_eaten[j] = True
				eaten_count += 1

	# print(snake_count, mongoose_count, eaten_count)
	snake_count -= eaten_count

	if snake_count == mongoose_count:
		ans.append("tie")
	elif snake_count > mongoose_count:
		ans.append("snakes")
	else:
		ans.append("mongooses")

for x in ans:
	print(x)