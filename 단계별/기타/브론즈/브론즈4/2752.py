import sys
input = sys.stdin.readline
lst = list(map(int, input().split()))
lst.sort()
for i in lst:
    print(i,end=' ')