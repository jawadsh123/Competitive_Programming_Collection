

n = int(input())
prime_list = []

ans = []

def sieve_of_eratosthenes(prime_range):
	global prime_list

	prime_bool = [True for j in range(prime_range+1)]
	curr = 2
	count = 2

	while curr < prime_range+1:
		if prime_bool[curr] == True:
			count = 2
		while curr*count < prime_range:
			prime_bool[curr*count] = False
			count += 1
		curr += 1

	prime_list = []
	for ele in range(2, prime_range+1):
		if prime_bool[ele]:
			prime_list.append(ele)

sieve_of_eratosthenes(1000000)
# print(prime_list)
x,y = 0,0
x_step, y_step = 0, -1
matrix_dim = 284
spiral_matrix = []

for i in range(matrix_dim**2):
	if x >= -matrix_dim/2 and x <= matrix_dim/2 and y >= -matrix_dim/2 and y <= matrix_dim/2:
		spiral_matrix.append((x,y))

	if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
		x_step, y_step = -y_step, x_step

	x += x_step
	y += y_step

# print(spiral_matrix)


for i in range(n):

	prime = int(input())

	for j, curr_prime in enumerate(prime_list):
		if curr_prime == prime:
			ans.append((spiral_matrix[j][0], spiral_matrix[j][1]))
			break
for x in ans:
	print(x[0], x[1])
