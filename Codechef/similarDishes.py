

t = int(input())
ans = []

for i in range(t):
	recipe_1 = list(input().split(' '))
	recipe_2 = list(input().split(' '))
	count = 0

	for ingredient in recipe_1:
		if ingredient in recipe_2:
			count += 1
	if count >= 2:
		ans.append("similar")
	else:
		ans.append("dissimilar")

for x in ans:
	print(x)