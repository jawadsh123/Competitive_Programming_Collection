
n = int(input())

catapults_array = []
catapults_position = []


for i in range(n):
	catapults_array.append(list(input().strip().split(",")))

def calc_movements(col=0):
	catapults_position = []
	for i in range(n):
		for j in range(n):
			if catapults_array[i][j] == "1":
				catapults_position.append((i, j))

	catapults_position.sort()
	total_moves = 0

	for target, position in enumerate(catapults_position):
		total_moves += abs(position[0]-target)
		total_moves += abs(position[1]-col)

	return total_moves

grand_total_moves = False

for col in range(n):
	curr_moves = calc_movements(col)
	# print(curr_moves)
	if grand_total_moves == False:
		grand_total_moves = curr_moves
	if curr_moves < grand_total_moves:
		grand_total_moves = curr_moves

print(grand_total_moves)



