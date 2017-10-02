

t = int(input())
ans = []

for i in range(t):

	n, k = list(map(int, input().split(' ')))
	island_ingredients = []
	ingredient_dict = [0 for j in range(k)]

	for j in range(n):
		ip = list(map(int, input().split(' ')))
		p = ip[0]
		island_ingredients.append(ip[1:])
		for ing in island_ingredients[j]:
			ingredient_dict[ing-1] += 1
	sadFlag = False

	for count in ingredient_dict:
		if count == 0:
			sadFlag = True
			break

	if sadFlag:
		ans.append("sad")
	else:
		someFlag = False
		for island in island_ingredients:
			islandRequired = False
			for ing in island:
				if ingredient_dict[ing-1] - 1 == 0:
					islandRequired = True
					break
			if islandRequired is False:
				someFlag = True
				break
		if someFlag:
			ans.append("some")
		else:
			ans.append("all")

for x in ans:
	print(x)
