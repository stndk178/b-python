import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    d = list(map(int, sys.stdin.readline().split()))
    lst.append(d)

lst.sort(key= lambda x : (x[0], x[1]))

for i in lst:
    for j in i:
        print(j, end=' ')
    print()