

a = [[0 for i in range(1030)] for j in range(1030)]

# fp = open("st-2.in", "r")
# fw = open("st-2.out", "w")

n, m, q = map(int, input().rstrip("\n").strip(' ').split(' '))
for i in range(1, n+1):
    ip = list(map(int, input().rstrip("\n").strip(' ').split(' ')))
    a[i][0] = 0
    for j in range(1, m+1):
        a[i][j] = ip[j-1]
for i in range(1,n+1):
    sum=0
    for j in range(1,m+1):
        sum=sum^a[i][j]
        a[i][j]=sum^a[i-1][j]
for i in range(q):
    r1, c1, r2, c2 = map(int, input().rstrip("\n").strip(' ').split(' '))
    maxx,maxy,minx,miny=0,0,0,0
    if c1>c2:
        maxx=c1
        minx=c2
    else:
        maxx=c2
        minx=c1
    if r1>r2:
        maxy=r1
        miny=r2
    else:
        maxy=r2
        miny=r1
    ans=a[miny][minx]^a[maxy+1][maxx+1]^a[maxy+1][minx]^a[miny][maxx+1]
    # fw.write(str(ans)+"\n")
    print(ans)

# fp.close()
# fw.close()
