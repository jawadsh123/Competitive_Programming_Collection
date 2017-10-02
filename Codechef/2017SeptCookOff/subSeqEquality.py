
t = int(input())
ans = []

for i in range(t):

    S = input()
    charCount = {}
    itsPossible = False

    for char in S:
        if char in charCount:
            charCount[char] += 1
            itsPossible = True
            break
        else:
            charCount[char] = 1
    
    if itsPossible:
        ans.append("yes")
    else:
        ans.append("no")

for x in ans:
    print(x)