import sys
n, m = map(int, sys.stdin.readline().split())
a = [[0 for j in range(m)] for i in range(n)]
b = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))


for i in range(n):
    b[i] = list(map(int, sys.stdin.readline().split()))


for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=' ')
    print()

#res = a+b이 안됨