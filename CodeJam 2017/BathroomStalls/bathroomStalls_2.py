from sortedcontainers import SortedList

ans = []
with open("C-small-2-attempt1.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]

t = int(content[0])

def split(number):
	"""splitting the numbers"""
	if number == 0:
		return [0, 0]
	if number%2 == 0:
		no1 = int(number/2)
		no2 = int(number/2 - 1)
	else:
		no1 = int((number-1)/2)
		no2 = int((number-1)/2)
	return [no1, no2]


for i in range(t):

	n, k = list(map(int, content[i+1].split(' ')))

	sortedList = SortedList()
	sortedList.add(n)

	for j in range(k-1):
		max_now = sortedList.pop()
		splitted = split(max_now)
		sortedList.add(splitted[0])
		sortedList.add(splitted[1])

	max_now = split(sortedList.pop())

	ans.append(max_now)

fw = open("C-small-2-attempt1.out", 'w')

for i, x in enumerate(ans):
	fw.write("Case #{0}: {1} {2}\n".format(i+1, x[0], x[1]))
