import random

t = int(input())
ans = []

for i in range(t):
    n, q = list(map(int, input().split()))
    connections = {}

    for j in range(q):
        u, v, val = list(map(int, input().split()))
        u -= 1
        v -= 1

        try:
            connections[u].append((v, val))
        except:
            connections[u] = [(v, val)]

        try:
            connections[v].append((u, val))
        except:
            connections[v] = [(u, val)]
    
    A = [-1 for _ in range(n)]
    # A = {}
    visited = [False for _ in range(n)]

    # keys = list(connections)
    keys = {}
    for x in list(connections):
        keys[x] = ""
    

    # curr = [keys[0]]
    remaining = connections.copy()

    # A[keys[0]] = 0
    idx = list(keys)[0]
    A[idx] = 0
    
    impossibleFlag = False
    
    while len(keys) > 0:
        # curr = [keys[0]]
        idx = list(keys)[0]
        A[idx] = 0
        curr = [idx]
        while len(curr) > 0:
            nextNodes = []

            for node in curr:

                try:
                    keys.pop(node)
                    # del keys[node]
                except:
                    pass

                if not visited[node]:
                    visited[node] = True
                # if node in connections:
                for neighbour, val in connections[node]:
                    try:
                        # if node in connections[neighbour]:
                        connections[neighbour].remove((node, val))
                        # print(node, val)
                    except:
                        pass
                    if not visited[neighbour]:
                        # if neighbour in connections:
                        if val == 1:
                            A[neighbour] = A[node] ^ 1
                        else:
                            A[neighbour] = A[node]
                        nextNodes.append(neighbour)
                        visited[neighbour] = True
                    else:
                        if (val == 1 and A[node] != A[neighbour]^1) or (val == 0 and A[node] != A[neighbour]):
                            impossibleFlag = True
                            break
                if impossibleFlag:
                    break
            if impossibleFlag:
                break
            
            curr = nextNodes.copy()


    
    if impossibleFlag:
        ans.append("no")
    else:
        ans.append("yes")

for x in ans:
    print(x)