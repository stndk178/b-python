import sys
d = []
for i in range(19):
    d.append(list(map(int,sys.stdin.readline().split())))

n = int(sys.stdin.readline())
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    x -=1
    y -=1
    for j in range(19):
        if(d[x][j]==1):
            d[x][j] = 0
        else:
            d[x][j] = 1

        if(d[j][y]==1):
            d[j][y] = 0
        else:
            d[j][y] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j] , end = ' ')
    print()
