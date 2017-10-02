
t = int(input())
ans = []

for i in range(t):

	s = input()
	longest_count = 0
	current_count = 0

	for j in range(len(s)):
		curr_char = s[j]
		if j == 0 and curr_char != "=":
			current_count += 1
			last_char = s[0]
		else:

			if curr_char != "=":
				if last_char == curr_char:
					current_count += 1
				else:
					# print(j)
					if current_count > longest_count:
						longest_count = current_count
					current_count = 1
				last_char = curr_char


	if current_count > longest_count:
		longest_count = current_count
	
	ans.append(longest_count+1)

for x in ans:
	print(x)
