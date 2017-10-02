
t = int(input())
ans = []

def key(diff):
    if diff == "cakewalk":
        return 0
    elif diff == "simple":
        return 1
    elif diff == "easy":
        return 2
    elif diff == "easy-medium":
        return 3
    elif diff == "medium":
        return 4
    elif diff == "medium-hard":
        return 5
    elif diff == "hard":
        return 6

for i in range(t):
    n = int(input())
    frequencyDict = dict()
    for j in range(7):
        frequencyDict[j] = 0

    for _ in range(n):
        difficulty = input()
        if difficulty in frequencyDict:
            frequencyDict[key(difficulty)] += 1
        else:
            frequencyDict[key(difficulty)] = 1

    impossibleFlag = False

    if frequencyDict[key("cakewalk")] < 1:
        impossibleFlag = True
    if frequencyDict[key("simple")] < 1:
        impossibleFlag = True
    if frequencyDict[key("easy")] < 1:
        impossibleFlag = True
    if not (frequencyDict[key("easy-medium")] >= 1 or frequencyDict[key("medium")] >= 1):
        impossibleFlag = True
    if not (frequencyDict[key("medium-hard")] >= 1 or frequencyDict[key("hard")] >= 1):
        impossibleFlag = True
    if impossibleFlag:
        ans.append("No")
    else:
        ans.append("Yes")


for x in ans:
    print(x)


