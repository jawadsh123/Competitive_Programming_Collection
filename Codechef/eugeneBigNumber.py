
t = int(input())

ans = []

exponents = []



def calc_exponents(x,e,m):
	if e == 0:
		exponents.append(1)
		return 1
	# elif e == 1:
	# 	exponents.append(x%m)
	# 	return x % m

	if e % 2 == 0:
		prod = calc_exponents(x, e//2, m)
		temp = (prod%m * prod%m) %m
	else:
		prod = calc_exponents(x, (e-1)//2, m)
		temp = ((prod%m * prod%m) %m * x % m) % m

	
	exponents.append(temp)
	return temp



def gp_sum(n, r, m, pt):

	if n == 1:
		return 1

	if n % 2 == 0:
		sn = (( 1 + exponents[pt] ) % m * gp_sum(n//2, r, m, pt - 1) ) % m
	else:
		sn = ((( 1 + exponents[pt] ) % m * gp_sum((n-1)//2, r, m, pt - 1) ) % m + (exponents[pt]%m * exponents[pt]%m) % m)

	# print(sn)
	return sn  



for i in range(t):

	a, n, m = list(map(int, input().split()))
	# a = 1000000000
	# n = 1000000000000
	# m = 1000000000

	length = len(str(a))

	r = pow(10, length)

	exponents = []

	calc_exponents(r, n, m)

	sum_part = gp_sum(n, r, m, len(exponents) - 2)

	total_prod = ( (a%m) * sum_part ) % m

	# print(total_prod, exponents)

	# print(sum_of_powers, a, total_prod)

	ans.append(total_prod)


for x in ans:
	print(x)