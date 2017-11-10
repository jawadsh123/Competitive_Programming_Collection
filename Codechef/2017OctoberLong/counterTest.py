import math

t = int(input())
ans = []

for _ in range(t):
    n = int(input())

    sizeOfSmallElements = math.floor((2**32-10**4)/(n))
    # print(2**32-10**4)

    sizeOfBigElement = ((2**32+2)-(sizeOfSmallElements*(n-2))) //2
    tempAns = [sizeOfBigElement]

    for _ in range(n-1):
        tempAns.append(sizeOfSmallElements)
    ans.append(tempAns)

    # print(sizeOfSmallElements, sizeOfBigElement)

for x in ans:
    print(*x)