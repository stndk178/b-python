import sys
input = sys.stdin.readline
res = []
for i in range(5):
    res.append(int(input()))

res.sort()
print(int(sum(res)/5))
print(res[2])