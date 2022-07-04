import sys
n = int(sys.stdin.readline())

s1 = set()
for i in range(n):
    num = int(sys.stdin.readline())
    s1.add(num)

s1 = list(s1)
s1.sort()


for item in s1:
    print(item)

