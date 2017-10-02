import math

t = int(input())
ans = []

for i in range(t):
	n = int(input())

	array = list(map(int, input().split(' ')))
	array_length = len(array)
	wrong_flag = False
	maxi_element = 0

	if array[0] != 1:
		wrong_flag = True
	else:
		going_up = True
		for j in range(1, array_length):
			diff = array[j] - array[j-1]

			if array[j] > maxi_element:
				maxi_element = array[j]

			if diff > 1 or diff < -1 or (diff == 1 and not going_up):
				wrong_flag = True
				break
			elif diff == -1 and going_up:
				going_up = False

		for j in range(array_length//2-1):
			if array[j] != array[array_length-j-1]:
				wrong_flag = True
				break

	if maxi_element != 7:
		wrong_flag = True

	if wrong_flag:
		ans.append("no")
	else:
		ans.append("yes")




for x in ans:
	print(x)
