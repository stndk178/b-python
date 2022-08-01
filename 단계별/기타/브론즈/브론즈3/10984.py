import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    s1 =0
    s2 =0
    for j in range(n):
        x,y = map(float,input().split())
        s1 += x
        s2 += x*y
    print(int(s1),round(s2/s1,1))