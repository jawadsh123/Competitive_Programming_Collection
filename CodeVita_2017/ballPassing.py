
k = int(input())

A_pos = list(input().split(' '))
xA, yA = int(A_pos[0]), int(A_pos[1])
B_pos = list(input().split(' '))
xB, yB = int(B_pos[0]), int(B_pos[1])

poles = []

for i in range(k):
	poles.append(list(input().split(' ')))

curr_no_of_steps = 0
curr_poles_hit = 0


def moveBall(lastMove, currX, currY):
	global curr_no_of_steps, curr_poles_hit

	if currX == xA and currY == yA:
		return curr_no_of_steps

	curr_no_of_steps += 1
	if curr_no_of_steps > k**2:
		return False

	if poles[currX][currY] == "0":
		if lastMove == "UP":
			if currX-1 < 0:
				return False
			else:
				return moveBall("UP", currX-1, currY)
		elif lastMove == "DOWN":
			if currX+1 >= k:
				return False
			else:
				return moveBall("DOWN", currX+1, currY)
		elif lastMove == "LEFT":
			if currY-1 < 0:
				return False
			else:
				return moveBall("LEFT", currX, currY-1)
		elif lastMove == "RIGHT":
			if currY+1 >= k:
				return False
			else:
				return moveBall("RIGHT", currX, currY+1)

	elif poles[currX][currY] == "1":
		if lastMove == "UP":
			if currY+1 >= k:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("RIGHT", currX, currY+1)
		elif lastMove == "DOWN":
			if currY-1 < 0:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("LEFT", currX, currY-1)
		elif lastMove == "LEFT":
			if currX+1 >= k:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("DOWN", currX+1, currY)
		elif lastMove == "RIGHT":
			if currX-1 < 0:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("UP", currX-1, currY)

			

	elif poles[currX][currY] == "2":
		if lastMove == "UP":
			if currY-1 < 0:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("LEFT", currX, currY-1)
		elif lastMove == "DOWN":
			if currY+1 >= k:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("RIGHT", currX, currY+1)
		elif lastMove == "LEFT":
			if currX-1 < 0:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("UP", currX-1, currY)
		elif lastMove == "RIGHT":
			if currX+1 >= k:
				return False
			else:
				curr_poles_hit += 1
				return moveBall("DOWN", currX+1, currY)

ans = []
temp_ans = moveBall("UP", xB, yB)
if temp_ans:
	ans.append((curr_no_of_steps, curr_poles_hit))
curr_no_of_steps, curr_poles_hit = 0, 0
# print(ans)

temp_ans = moveBall("LEFT", xB, yB)
if temp_ans:
	ans.append((curr_no_of_steps, curr_poles_hit))
curr_no_of_steps, curr_poles_hit = 0, 0
# print(ans)

temp_ans = moveBall("RIGHT", xB, yB)
if temp_ans:
	ans.append((curr_no_of_steps, curr_poles_hit))
curr_no_of_steps, curr_poles_hit = 0, 0
# print(ans)

temp_ans = moveBall("DOWN", xB, yB)
if temp_ans:
	ans.append((curr_no_of_steps, curr_poles_hit))
curr_no_of_steps, curr_poles_hit = 0, 0

if len(ans) > 0:
	ans.sort()
	print(ans[0][0], ans[0][1])
else:
	print(-1)
	


