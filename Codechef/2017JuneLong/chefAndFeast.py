
t = int(input())
ans = []

for i in range(t):

	n = int(input())
	happiness = list(map(int, input().split(' ')))

	total_sadness = 0
	total_happiness = 0
	number_of_happy = 0

	for x in happiness:
		if x >= 0:
			total_happiness += x
			number_of_happy += 1
		else:
			total_sadness -= x

	total_emotion = number_of_happy * total_happiness - total_sadness
	ans.append(total_emotion)

for x in ans:
	print(x)