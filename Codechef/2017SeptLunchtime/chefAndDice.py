
t = int(input())
ans = []



for i in range(t):
    n = int(input())

    A = list(map(int, input().strip(' ').split(' ')))

    adjacencyList = {}
    possibleList = {}
    reservedEle = set()
    finalOpposites = [0 for _ in range(7)]

    def findOpposites(depth):
        global possibleList
        # print(depth, reservedEle)
        if depth != 1:
            if depth in reservedEle:
                return findOpposites(depth-1)
            else:
                reservedEle.add(depth)
                for ele in possibleList[depth]:
                    if ele not in reservedEle:
                        reservedEle.add(ele)
                        val = findOpposites(depth-1)
                        if val == False:
                            reservedEle.discard(ele)
                        else:
                            finalOpposites[depth] = ele
                            finalOpposites[ele] = depth
                            return True
                reservedEle.discard(depth)
                return False
        else:
            if depth in reservedEle:
                return True
            else:
                return False
        # if depth in reservedEle and depth != 6:
        #     return findOpposites(depth+1)
        # elif depth in reservedEle and depth == 6:
        #     return True
        # # elif depth == 6 and depth not in reservedEle:
        # #     return False
        # else:
            
        # return False

    possibleFlag = True
    
    for j in range(7):
        adjacencyList[j] = set()
        adjacencyList[j].add(j)
    
    for j in range(len(A)):
        if len(A) == 1:
            break
        if j == 0 and j != n-1:
            if A[j] == A[j+1]:
                possibleFlag = False
                break
            adjacencyList[A[j]].add(A[j+1])
        elif j == n-1 and j != 0:
            if A[j] == A[j-1]:
                possibleFlag = False
                break
            adjacencyList[A[j]].add(A[j-1])
        else:
            # print(A[j], A[j-1], A[j+1])
            if A[j] == A[j-1] or A[j] == A[j+1]:
                possibleFlag = False
                break
            adjacencyList[A[j]].add(A[j-1])
            adjacencyList[A[j]].add(A[j+1])
        
    if possibleFlag == True:
        for j in range(7):
            possibleList[j] = set()
        
        for key in adjacencyList:
            for j in range(1,7):
                if j not in adjacencyList[key]:
                    possibleList[key].add(j)
        
        possibleFlag = findOpposites(6)
        if possibleFlag == False:
            ans.append(-1)
        else:
            ans.append(finalOpposites)
    else:
        ans.append(-1)

for x in ans:
    if x == -1:
        print(-1)
    else:
        print(*x[1:])