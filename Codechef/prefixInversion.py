

s = input()
count = 0

looking_for = "1"

def toggle_looking_for():
	global looking_for

	if looking_for == "1":
		looking_for = "0"
	else:
		looking_for = "1"

for index in range(len(s)-1, -1, -1):
	character = s[index]

	if character == looking_for:
		count += 1
		toggle_looking_for()


print(count)
