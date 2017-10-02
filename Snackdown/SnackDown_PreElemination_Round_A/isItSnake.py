t = int(input())
ans = []

def toggle_side(val):
	return 0 if val == 1 else 1

for i in range(t):

	n = int(input())

	plate = [0, 0]

	plate[0] = input()
	plate[1] = input()
	both_side_found = False
	curr_side = 0

	traversing_snake = False
	snake_finished = False
	not_possible = False

	snake_started = False

	for j in range(n):

		if snake_finished:
			if plate[0][j] == "#" or plate[1][j] == "#":
				not_possible = True
				break
		elif traversing_snake:
			if plate[curr_side][j] == "#":
				if plate[toggle_side(curr_side)][j] == "#":
					curr_side = toggle_side(curr_side)
			else:
				if plate[toggle_side(curr_side)][j] == "#":
					not_possible = True
					break
				snake_finished = True
		elif (plate[0][j] == "#" and plate[1][j] == "."):
			traversing_snake = True
			curr_side = 0
		elif (plate[0][j] == "." and plate[1][j] == "#"):
			traversing_snake = True
			curr_side = 1
		elif (plate[0][j] == "#" and plate[1][j] == "#"):
			snake_started = True

		elif (plate[0][j] == "." and plate[1][j] == ".") and snake_started:
			snake_finished = True

	if not_possible:
		ans.append("no")
	else:
		ans.append("yes")

for x in ans:
	print(x)


