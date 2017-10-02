import math
fp = open("st-1.in", "r")
r,c,q=[int(x) for x in fp.readline().strip().split(" ")]
xi=[]
for x in range(r):
	xi.append([int(x) for x in fp.readline().strip().split(" ")])
# print(len(xi[0]))
bits=0
for x in range(q):
	rx,cx,rx1,cx1=[int(j) for j in fp.readline().strip().split(" ")]
	# print(rx,cx,rx1,cx1)
	temp=[]
	for k in range(rx1+1):
		temp.append([int(0) for j in range(cx1+1)])	
	print("Length",len(temp))
	for i in range(rx,rx1+1):
		for j in range(cx,cx1+1):
			# temp[i][j] = temp[i][j]
			# print(i, j)
			temp[i][j]=(bits ^ xi[i][j])
			bits=temp[i][j]
	print(temp[rx1][cx1])	

# 366 633
