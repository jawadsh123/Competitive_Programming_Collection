
t = int(input())
ans = []

for i in range(t):
    n = int(input())

    goodPermutation = []
    if n%2 == 0:
        for j in range(n):
            if j%2 == 0:
                goodPermutation.append(j+1+1)
            else:
                goodPermutation.append(j+1-1)
    else:
        for j in range(n-3):
            if j%2 == 0:
                goodPermutation.append(j+1+1)
            else:
                goodPermutation.append(j+1-1)
        goodPermutation.append(n-1)
        goodPermutation.append(n)
        goodPermutation.append(n-2)

    ans.append(goodPermutation)

for x in ans:
    for ele in x:
        print(ele, end=" ")
    print("")
