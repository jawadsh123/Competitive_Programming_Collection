
t = int(input())
ans = []

for i in range(t):
	l = int(input())
	report = input()

	head_flag = False
	invalid_flag = False

	for entry in report:
		if entry == "H":
			if head_flag == True:
				invalid_flag = True
				break
			else:
				head_flag = True
		elif entry == "T":
			if head_flag == True:
				head_flag = False
			else:
				invalid_flag = True
				break

	if head_flag == True or invalid_flag == True:
		ans.append("Invalid")
	else:
		ans.append("Valid")

for x in ans:
	print(x)