import math

n, q = list(map(int, input().split()))
connections = {}
visited = [False for i in range(n)]
powers = []
ans = []

def calcPowersOfTwo():
    global powers

    currPower = 2
    powers.append(currPower)
    while currPower < 1000000:
        currPower = currPower << 1
        powers.append(currPower)

for i in range(n-1):
    u, v = list(map(int, input().split()))
    try:
        connections[u].append(v)
    except:
        connections[u] = [v]
    
    try:
        connections[v].append(u)
    except:
        connections[v] = [u]

X = list(map(int, input().split()))

depth = 0
levelXor = []
curr = [0]

while len(curr) > 0:
    nextNodes = []
    currXor = 0

    for node in curr:

        currXor ^= X[node]
        if not visited[node]:
            visited[node] = True
        # if node in connections:
        for neighbour in connections[node]:
            if not visited[neighbour]:
                # if neighbour in connections:
                try:
                    # if node in connections[neighbour]:
                    connections[neighbour].remove(node)
                except:
                    pass
                nextNodes.append(neighbour)
                visited[neighbour] = True
    curr = nextNodes.copy()
    levelXor.append(currXor)
    depth += 1

prefixSum = []
# suffixSum = [0 for _ in range(depth)]
# sumXor 
prefixSumAlter = []
# suffixSumAlter = [0 for _ in range(math.ceil(depth/2))]

# Normal prefix Xor sum
for ele in levelXor:
    if len(prefixSum) > 0:
        prefixSum.append(prefixSum[-1]^ele)
    elif len(prefixSumAlter) == 0:
        prefixSum.append(ele)

# Alternating prefix XOR sum
for idx, ele in enumerate(levelXor):
    if len(prefixSumAlter) > 0 and idx%2 == 0:
        prefixSumAlter.append(prefixSumAlter[-1]^ele)
    elif len(prefixSumAlter) > 0 and idx%2 == 1:
        prefixSumAlter.append(prefixSumAlter[-1])
    elif len(prefixSumAlter) == 0:
        prefixSumAlter.append(ele)

# Normal suffix Xor sum
# for idx in range(depth-1, -1, -1):
#     if idx == depth-1:
#         suffixSum[idx] = levelXor[idx]
#     else:
#         suffixSum[idx] = suffixSum[idx+1]^levelXor[idx]

# # Alternating suffix xor sum
# for idx in range(depth-1, -1, -1):
#     if (idx == depth-1 or idx == depth-2) and idx%2 == 0:
#         suffixSumAlter[idx//2] = levelXor[idx//2]
#     elif idx%2 == 0:
#         suffixSumAlter[idx//2] = suffixSumAlter[idx//2+1]^levelXor[idx//2]


# All the game is about powers of 2
calcPowersOfTwo()

maxIteration = 0
for power in powers:
    if power >= depth:
        maxIteration = power
        break
# print(maxIteration)
memoizedVals = {}

for i in range(q):
    iteration = int(input())-1
    
    if iteration == -1:
        ans.append(levelXor[0])
        continue
    iteration = iteration % maxIteration
    powerList = []
    tempVal = iteration

    # Encountered this val before
    if iteration in memoizedVals:
        ans.append(memoizedVals[iteration])
        continue

    # TODO Test
    while (tempVal != 0 and tempVal != 1) and tempVal > 1:
        # print(tempVal)
        closeMinPower = 0
        for power in powers:
            if power <= tempVal:
                closeMinPower = power
            else:
                break
        powerList.append(closeMinPower)
        diff = tempVal - closeMinPower
        tempVal = diff
    
    if tempVal == 0:
        pref = prefixSum
        # suff = suffixSum
    else:
        pref = prefixSumAlter
        # suff = suffixSumAlter
    
    xorSum = 0
    if len(powerList) > 0:
        powerList = powerList[::-1]
        val = -1
        jump = powerList[0]
        left = -1
        right = 0

        while val <= depth-1:
            right = left + powerList[0]
            if right > depth-1:
                right = depth-1
            if left == -1:
                xorSum ^= pref[right]
            else:
                xorSum ^= pref[right] ^ pref[left]
            val += powerList[0]
            for power in powerList:
                if (val+1)%power == 0:
                    val += power
                else:
                    break
            left = val
    else:
        xorSum = pref[depth-1]

    memoizedVals[iteration] = xorSum
    ans.append(xorSum)

    # print(xorSum)
for x in ans:
    print(x)
# print(levelXor, prefixSum, prefixSumAlter, maxIteration)

