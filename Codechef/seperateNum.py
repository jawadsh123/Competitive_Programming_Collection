
q = int(input())



for i in range(q):
	s = input()
	for j in range(len(s)//2):
		first_num = int(s[0:j+1])
		next_num = first_num + 1
		while s[j: ]