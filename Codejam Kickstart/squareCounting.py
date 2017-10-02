
# t = int(input())

with open("A-small-attempt1.in") as f:
    content = f.readlines()

content = [x.strip() for x in content]

t = int(content[0])

ans = []

MOD = 1000000007

for i in range(t):
	r, c = list(map(int, content[i+1].split(' ')))

	r -= 1
	c -= 1

	if r > c:
		l = r
		s = c
	else:
		l = c
		s = r

	tot_sq = 0

	for j in range(1, s+1):

		no_of_sq = ((l-(j-1))%MOD * (s-(j-1))%MOD)%MOD
		no_of_sq += ((l-(j-1))%MOD * (s-(j-1))%MOD * (j-1)%MOD)%MOD

		# print(no_of_sq)

		tot_sq += no_of_sq%MOD

	tot_sq %= MOD


	ans_str = "Case #" + str(i+1) + ": " + str(tot_sq)
	ans.append(ans_str)

fw = open('myfile-Large.out', 'w') 

for x in ans:
	fw.write(x + '\n')