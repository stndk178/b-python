import sys
input = sys.stdin.readline
n = int(input())
res = ''
for i in range(n):
    s = input().rstrip()
    res=s[1:]
    print(s[0].upper()+res)