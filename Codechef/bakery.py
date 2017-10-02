


t = int(input())
ans = []


for i in range(t):
    n, x = list(map(int, input().split()))
    if n%x == 0:
        ans.append(x)
    else:
        ans.append(n%x)

for x in ans:
    print(x)