
n = int(input("Height of tree: "))
iteration = int(input("Iteration: "))

initial = [set(chr(i+65)) for i in range(n)]

last = initial.copy()
curr = initial.copy()

all_patterns = []

grandSum = 0
for k in range(iteration):
    for i in range(n):
        for j in range(i+1, n):
            curr_set = curr[i]
            curr[i] = set.union(curr_set, last[j])
            curr[i] -= set.intersection(curr_set, last[j])
    last = curr

    # print("=====================")
    # print("Iteration: ", k)
    # for ele in curr:
        # print(sorted(ele))

    pattern = ""
    for idx in range(n):
        # print(min(initial[idx]), curr[0])
        if min(initial[idx]) in curr[0]:
            # pattern += "1"
            grandSum += 1
        # else:
            # pattern += "0"
    all_patterns.append(pattern)
    
print("======================")
print("Patterns")
for pattern in all_patterns:
    print(pattern)
print(grandSum)
