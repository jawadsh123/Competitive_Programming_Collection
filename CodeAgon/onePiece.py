
xt, yt = list(map(int, input().split()))

n = int(input())

for i in range(n):
	dx, dy = list(map(int, input().split()))
	xt -= dx
	yt -= dy

print(xt, yt)