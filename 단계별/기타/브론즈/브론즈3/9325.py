import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    res = 0
    s = int(input())
    n = int(input())
    for j in range(n):
        q,p = map(int,input().split())
        res += q*p
    print(res+s)