import sys
input = sys.stdin.readline

s = input().rstrip()
r = ["a","e","i","o","u"]
cnt = 0
for i in r:
    cnt += s.count(i)

print(cnt)