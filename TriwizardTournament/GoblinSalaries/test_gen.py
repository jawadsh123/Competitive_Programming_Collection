import random as ran

t = 5
print(t)
max_range = 1000000

for i in range(t):
	l = ran.randrange(max_range)
	if l+1000000+1 < max_range:
		b = ran.randrange(l, l+1000000+1)
	else:
		b = ran.randrange(l, max_range+1)
	# print(b-l)
	print(l, b)