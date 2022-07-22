import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    lst = input().split()
    for i in range(len(lst)-1):
        res = lst[i]
        print(res[::-1],end=' ')
    res = lst[-1]
    print(res[::-1])



