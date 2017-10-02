t=int(input())
i=0
while i < t:
    ip=str(input())
    ans=[]
    for x in range(65,91):
        if(x==66 or x==77 or x==88):
            if(ip.count(str(x%10))>=2 and ip.count(str(int(x/10)))>=2):
                ans.append(chr(x))
        else:        
            if(ip.count(str(x%10))>=1 and ip.count(str(int(x/10)))>=1):
                ans.append(chr(x))
    print(''.join(str(x) for x in ans))            
    i+=1






















