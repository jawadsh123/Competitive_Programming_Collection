
t = int(input())
ans = []

for i in range(t):
	x11, y11, x12, y12 = list(map(int, input().split(' ')))
	x21, y21, x22, y22 = list(map(int, input().split(' ')))

	if x11-x12 == 0 and y11-y12 == 0:
		if x21 > x22:
			higher_x2 = x21
			lower_x2 = x22
		else:
			higher_x2 = x22
			lower_x2 = x21
		if y21 > y22:
			higher_y2 = y21
			lower_y2 = y22
		else:
			higher_y2 = y22
			lower_y2 = y21

		if (x11 >= lower_x2 and x11 <= higher_x2) and (y11 >= lower_y2 and y11 <= higher_y2):
			ans.append("yes")
			continue
		else:
			ans.append("no")
			continue
	elif x21-x22 == 0 and y21-y22 == 0:
		if x11 > x12:
			higher_x1 = x11
			lower_x1 = x12
		else:
			higher_x1 = x12
			lower_x1 = x11
		if y11 > y12:
			higher_y1 = y11
			lower_y1 = y12
		else:
			higher_y1 = y12
			lower_y1 = y11

		if (x21 >= lower_x1 and x21 <= higher_x1) and (y21 >= lower_y1 and y21 <= higher_y1):
			ans.append("yes")
			continue
		else:
			ans.append("no")
			continue
	elif y11 - y12 == 0:
		if x11 > x12:
			higher_x1 = x11
			lower_x1 = x12
		else:
			higher_x1 = x12
			lower_x1 = x11
		# first is horizontal
		if y21 - y22 == 0:
			if x21 > x22:
				higher_x2 = x21
				lower_x2 = x22
			else:
				higher_x2 = x22
				lower_x2 = x21
			# second is horizontal too ..... YAAY?
			if y11 != y21:
				# on diff rows
				ans.append("no")
				continue
			else:
				# overlapping
				if (lower_x2 >= lower_x1 and lower_x2 <= higher_x1) or (higher_x2 >= lower_x1 and higher_x2 <= higher_x1) or (lower_x1 >= lower_x2 and lower_x1 <= higher_x2) or (higher_x1 >= lower_x2 and higher_x1 <= higher_x2):
					ans.append("yes")
					continue
				else:
					ans.append("no")
					continue
		else:
			# second aint horizontal
			if x21 == higher_x1 or x21 == lower_x1:
				# at end points of first
				if y21 == y11 or y22 == y11:
					# exactly at end points
					ans.append("yes")
					continue
				else:
					ans.append("no")
					continue
			else:
				ans.append("no")
				continue
	elif x11 - x12 == 0:
		if y11 > y12:
			higher_y1 = y11
			lower_y1 = y12
		else:
			higher_y1 = y12
			lower_y1 = y11
		# first is horizontal
		if x21 - x22 == 0:
			if y21 > y22:
				higher_y2 = y21
				lower_y2 = y22
			else:
				higher_y2 = y22
				lower_y2 = y21
			# second is horizontal too ..... YAAY?
			if x11 != x21:
				# on diff rows
				ans.append("no")
				continue
			else:
				# overlapping
				if (lower_y2 >= lower_y1 and lower_y2 <= higher_y1) or (higher_y2 >= lower_y1 and higher_y2 <= higher_y1) or (lower_y1 >= lower_y2 and lower_y1 <= higher_y2) or (higher_y1 >= lower_y2 and higher_y1 <= higher_y2):
					ans.append("yes")
					continue
				else:
					ans.append("no")
					continue
		else:
			# second aint horizontal
			if y21 == higher_y1 or y21 == lower_y1:
				# at end points of first
				if x21 == x11 or x22 == x11:
					# exactly at end points
					ans.append("yes")
					continue
				else:
					ans.append("no")
					continue
			else:
				ans.append("no")
				continue

for x in ans:
	print(x)