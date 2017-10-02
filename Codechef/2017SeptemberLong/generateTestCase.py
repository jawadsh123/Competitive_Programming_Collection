n = 100000
q = 100000

fp = open("ip.in", "w")

fp.write(str(n)+" "+str(q)+"\n")
# print(n, q)
for i in range(n-1):
    # print(i, i+1)
    fp.write(str(i)+" "+str(i+1)+"\n")

for i in range(n):
    # print(i+1, end=" ")
    fp.write(str(i+1)+" ")
# print()
fp.write("\n")

for i in range(q):
    # print(i+1000)
    fp.write(str(i+1000)+"\n")