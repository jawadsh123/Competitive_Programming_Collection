t=int(input())
i=0
while i<t:
	l,b=[int(x) for x in input().split(" ")]
	if(l<b):
		min=l
		max=b
	else:
		min=b
		max=l		
	while max%min!=0:
		# print(max, min)
		print(str(min)+" "+str(int(max/min)))
		max=max-min
		max,min=min,max

	print(str(min)+" "+str(int(max/min)))
	i+=1
