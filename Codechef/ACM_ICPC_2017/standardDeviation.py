# Author: Aditya 

import math
t = int(input())
while t:
    t=t-1
    a = [int(x) for x in input().strip(' ').split(' ')]
    n = a[0]
    sd = a[1]

    if n == 1:
        if sd == 0:
            print("0")
        else:
            print("-1")
    else:
        lhs = math.sqrt( (n**2)*(sd**2) / (n-1))
        for i in range(n):
            if i==0:
                print(lhs,end=" ")
            else:
                print(0,end=" ")
        print("")