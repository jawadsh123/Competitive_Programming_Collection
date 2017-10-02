
n = int(input().strip())
unsorted = []
unsorted_i = 0

max_len = 0

for unsorted_i in range(n):
	unsorted_t = str(input().strip())
	curr_len = len(unsorted_t)
	if curr_len > max_len:
		max_len = curr_len
	unsorted.append(unsorted_t)

for j in range(n):
	unsorted[j] = unsorted[j].zfill(max_len)

unsorted.sort()

for x in unsorted:
	print(x.lstrip('0'))