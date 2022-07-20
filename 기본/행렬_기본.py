import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #n:행  m:열
#res = [[0 for i in range(m)] for j in range(n)]
res = []
for i in range(n):
    t = list(map(int,input().split()))
    res.append(t)

for i in range(n):
    for j in range(m):
        print(res[i][j],end= ' ')
    print()


''' 이렇게 입력받음
n,m = map(int,input().split())
for i in range(n):
    data = list(map(int,input().split()))

'''