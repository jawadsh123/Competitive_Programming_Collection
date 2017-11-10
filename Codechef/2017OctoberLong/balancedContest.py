
t = int(input())
ans = []

for i in range(t):
    n, p = list(map(int, input().split(' ')))
    numOfSolutions = list(map(int, input().split(' ')))
    countOfCakewalkProblems = 0
    countOfHardProblems = 0

    for num in numOfSolutions:

        if num >= p//2:
            countOfCakewalkProblems += 1
        if num <= p//10:
            countOfHardProblems += 1

    if countOfCakewalkProblems == 1 and countOfHardProblems == 2:
        ans.append("yes")
    else:
        ans.append("no")
    
for x in ans:
    print(x)