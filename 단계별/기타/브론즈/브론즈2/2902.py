import sys
input = sys.stdin.readline
s = list(input().split("-"))
for i in range(len(s)):
    print(s[i][0],end="")