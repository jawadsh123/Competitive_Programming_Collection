
t = int(input())
ans = []

for i in range(t):

    n, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    present = [False for j in range(k)]

    for number in numbers:
        binary = bin(number)
        idx = 0
        if number != 0 and (number & (number-1)) == 0:
            present[len(binary)-2-1] = True
    
    count = 0
    for cond in present:
        if cond == False:
            count += 1
    
    if count == 0:
        ans.append(0)
    else:
        ans.append(count)

for x in ans:
    print(x)