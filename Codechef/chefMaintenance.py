
t = int(input())

ans = []

for i in range(t):
	number = int(input())
	n = list(map(int, input().split()))

	start_stacking = False

	unpaid_amount = 0

	for x in n:
		if x == 0:
			unpaid_amount += 1100
			if start_stacking == False :
				start_stacking = True
		if x == 1:
			if start_stacking:
				unpaid_amount += 100

	ans.append(unpaid_amount)

for x in ans:
	print(x)
