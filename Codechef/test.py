import time


start = time.clock()


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
		sn = (( 1 + pow(r, n//2, m) ) % m * gp_sum(n//2, r, m) ) % m
	else:
		sn = ((( 1 + pow(r, (n-1)//2, m)) % m * gp_sum((n-1)//2, r, m) ) % m + pow(r, n-1, m)) % m


	return sn  


print(calc_exponents(10, 6, 10000000000), exponents)
# print(pow(2,4,100))



end = time.clock()

print(end - start)