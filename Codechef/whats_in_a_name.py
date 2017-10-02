
ans = []
t = int(input())

for i in range(t):

	complete_name = list(input().split(" "))
	number_of_parts = len(complete_name)

	final_name = ""

	for j in range(number_of_parts-1):
		part = complete_name[j].upper()[0]
		final_name += part + ". "

	last_part = complete_name[-1].title()

	final_name += last_part
	ans.append(final_name)

for x in ans:
	print(x)
