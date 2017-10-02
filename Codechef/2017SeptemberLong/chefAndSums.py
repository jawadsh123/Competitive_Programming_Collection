
t = int(input())
ans = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    prefixSum = []
    suffixSum = []
    
    tempPrefix = 0
    for j in range(n):
        tempPrefix += a[j]
        prefixSum.append(tempPrefix)

    tempSuffix = 0
    for j in range(n-1, -1, -1):
        tempSuffix += a[j]
        suffixSum.append(tempSuffix)
    suffixSum.reverse()

    minimum = False
    idx = 0
    for j in range(n):
        curr = prefixSum[j] + suffixSum[j]
        if minimum is False or curr < minimum:
            minimum = curr
            idx = j

    ans.append(idx+1)

for x in ans:
    print(x)
