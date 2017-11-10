
t = int(input())
ans = []

for i in range(t):

    scores = []
    for _ in range(3):
        s1, s2, s3 = list(map(int, input().split(' ')))
        scores.append([s1, s2, s3])


    notPossible = False
    lessThan = False
    atleastOneGreater = False
    for j in range(3):
        if scores[0][j] < scores[1][j]:
            lessThan = True
        if scores[0][j] > scores[1][j]:
            atleastOneGreater = True
    
    if lessThan and atleastOneGreater or (not lessThan and not atleastOneGreater):
        ans.append("no")
        notPossible = True

    if not notPossible:
        lessThan = False
        atleastOneGreater = False
        for j in range(3):
            if scores[1][j] < scores[2][j]:
                lessThan = True
            if scores[1][j] > scores[2][j]:
                atleastOneGreater = True
        
        if lessThan and atleastOneGreater or (not lessThan and not atleastOneGreater):
            ans.append("no")
            notPossible = True
        
    if not notPossible:
        lessThan = False
        atleastOneGreater = False
        for j in range(3):
            if scores[0][j] < scores[2][j]:
                lessThan = True
            if scores[0][j] > scores[2][j]:
                atleastOneGreater = True
        
        if lessThan and atleastOneGreater or (not lessThan and not atleastOneGreater):
            ans.append("no")
            notPossible = True

    if not notPossible:
        ans.append("yes")

for x in ans:
    print(x)