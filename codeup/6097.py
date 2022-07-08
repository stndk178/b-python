h,w = map(int, input().split())
res = [[0 for i in range(w)] for j in range(h)]

n = int(input())
for i in range(n):
    l,d,x,y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(l):
        if d==0:
            res[x][y+j] = 1
        else:
            res[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(res[i][j],end=' ')
    print()