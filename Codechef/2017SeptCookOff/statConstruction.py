
t = int(input())
ans = []

for i in range(t):

    n = int(input())
    temp_ans = []

    if n%2 == 1:
        for j in range(n-n//2, n+n//2+1):
            temp_ans.append(j)
    else:
        for j in range(n-n//2, n):
            temp_ans.append(j)
        for j in range(n+1, n+n//2+1):
            temp_ans.append(j)
    
    ans.append(temp_ans)

for x in ans:
    print(*x)