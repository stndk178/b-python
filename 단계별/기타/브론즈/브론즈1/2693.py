import sys
input = sys.stdin.readline
for i in range(int(input())):
    res = list(map(int,input().split()))
    res.sort()
    print(res[-3])