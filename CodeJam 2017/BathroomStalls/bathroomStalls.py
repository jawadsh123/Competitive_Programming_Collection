
ans = []
with open("C-large.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]

t = int(content[0])


def split(number):
	"""splitting the numbers"""
	if number == 0:
		return [0, 0]
	if number%2 == 0:
		no1 = int(number/2 - 1)
		no2 = int(number/2)
	else:
		no1 = int((number-1)/2)
		no2 = int((number-1)/2)
	return [no1, no2]

class node(object):

	mini = 0
	maxi = 0
	count = 0

	def __init__(self, ele1, ele2, count):
		super(node, self).__init__()
		if ele1 > ele2:
			self.mini = ele2
			self.maxi = ele1
		else:
			self.mini = ele1
			self.maxi = ele2
		self.count = count


for i in range(t):
	n, k = list(map(int, content[i+1].split(' ')))
	Lcount = 1
	Rcount = 1

	remaining_people = k
	splitted = split(n)
	count = 1
	remaining_people -= 1
	if k == 1:
		temp_ans = []
		if splitted[0] > splitted[1]:
			temp_ans = [splitted[0], splitted[1]]
		else:
			temp_ans = [splitted[1], splitted[0]]
		ans.append(temp_ans)
	else:

		while remaining_people >= 0:
			# print("Splitted: ",splitted)
			
			node_1 = split(splitted[0])
			node_1 = node(node_1[0], node_1[1], Lcount)

			node_2 = split(splitted[1])
			node_2 = node(node_2[0], node_2[1], Rcount)

			layer_sum = node_1.count + node_2.count
			if remaining_people <= layer_sum:
				if remaining_people <= node_2.count:
					ans.append([node_2.maxi, node_2.mini])
				else:
					ans.append([node_1.maxi, node_1.mini])
				break

			next_splitted = [0, 0]

			if splitted[0]%2 == 0 and splitted[1]%2 == 0:
				newLcount = Lcount + Rcount
				newRcount = Lcount + Rcount
				next_splitted[0] = node_1.mini
				next_splitted[1] = node_1.maxi
			elif splitted[0]%2 == 1 and splitted[1]%1 == 1:
				newLcount = 2*Lcount
				newRcount = 2*Rcount
				next_splitted[0] = node_1.mini
				next_splitted[1] = node_1.maxi
			elif splitted[0]%2 == 1:
				newLcount = 2 * Lcount + Rcount
				newRcount = Rcount
				next_splitted[0] = node_2.mini
				next_splitted[1] = node_2.maxi
			else:
				newLcount = Lcount
				newRcount = 2*Rcount + Lcount
				next_splitted[0] = node_1.mini
				next_splitted[1] = node_1.maxi

			splitted = next_splitted
			Lcount = newLcount
			Rcount = newRcount
			remaining_people -= layer_sum
			# print(node_1.mini, node_1.maxi, node_2.mini, node_2.maxi)
			# print("remaining: ", remaining_people)

fw = open("C-large.out", 'w')

for i, x in enumerate(ans):
	fw.write("Case #{0}: {1} {2}\n".format(i+1, x[0], x[1]))





