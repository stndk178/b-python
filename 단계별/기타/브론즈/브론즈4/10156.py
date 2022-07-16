import sys
input = sys.stdin.readline
k,n,m = map(int,input().split())

res = k*n
res -= m
if res<0:
    print(0)
else:
    print(res)