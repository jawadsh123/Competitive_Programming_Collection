
t = int(input())
ans = []

for i in range(t):

    n, k = list(map(int, input().split(' ')))
    totalSum = 0

    for j in range(n):
        length = (j+1)*2
        
        elemPerm = k
        for _ in range(j):
            elemPerm *= (k-1)
        
        splitPerm = 1
        if j != 0:
            for idx in range(n-1, j, -1):
                splitPerm *= idx
        totalSum += length*elemPerm*splitPerm
    
    print(totalSum/k**n)
