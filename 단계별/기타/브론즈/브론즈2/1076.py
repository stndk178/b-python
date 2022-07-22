import sys
input = sys.stdin.readline
res = ["black","brown","red","orange","yellow", "green", "blue", "violet", "grey","white"]
r = []
for i in range(3):
    r.append(input().rstrip())

a = res.index(r[0])
b = res.index(r[1])
c = res.index(r[2])
print((a*10+b)*(10**c))