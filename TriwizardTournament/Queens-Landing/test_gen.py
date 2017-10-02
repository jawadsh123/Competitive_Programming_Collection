import random as ran


fp = open("st-2.in", "w")

Q = ran.randrange(1000000)

dim = 1000
R = ran.randrange(1, dim)
C = ran.randrange(1, dim)

pit = [[ran.randrange(1, 100) for i in range(C)] for j in range(R)]

fp.write("{} {} {}\n".format(R, C, Q))
print("{} {} {}".format(R, C, Q))
for row in pit:
	for ele in row:
		fp.write(str(ele)+" ")
		# print(ele, end=" ")
	# print()
	fp.write("\n")

for j in range(Q):
	x1 = ran.randrange(R-1)
	y1 = ran.randrange(C-1)
	x2 = ran.randrange(x1, R)
	y2 = ran.randrange(y1, C)
	fp.write("{} {} {} {}\n".format(x1, y1, x2, y2))
	# print(x1, y1, x2, y2)