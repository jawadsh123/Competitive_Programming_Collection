fp = open("tests1.txt", "r")
t=int(fp.readline())
i=0
while i<t:
	ans=0
	ip=fp.readline().strip()
	ip=[int(x) for x in ip]
	ip.reverse()
	cond=True
	while cond:
		l=ip.index(1)
		for x in range(l,len(ip)):
			ip[x]=1-ip[x]
		ans+=1
		if(sum(ip)==0):
			cond=False
	print(ans)
	i+=1