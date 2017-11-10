
t = int(input())
ans = []

for _ in range(t):

    n, k = list(map(int, input().split(' ')))
    s = list(map(int, input().split(' ')))

    elementPresent = [False for _ in range(2*10**6)]

    for ele in s:
        elementPresent[ele] = True

    noMoreAdditions = False
    ansFound = False
    for ele in range(len(elementPresent)):
        if k == 0:
            noMoreAdditions = True

        if not noMoreAdditions:
            if not elementPresent[ele]:
                k -= 1
                elementPresent[ele] = True
        else:
            if not elementPresent[ele]:
                ans.append(ele)
                break
            else:
                continue
        

for x in ans:
    print(x)