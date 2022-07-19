import sys
input = sys.stdin.readline
n = int(input())
t = [300,60,10]
res = [0]*3
for i in range(3):
    res[i] = n//t[i]
    n %= t[i]

if n==0:
    print(res[0],res[1],res[2])
else:
    print(-1)
